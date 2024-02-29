import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

# Import system and the nodes/elements
System = pd.read_csv('Simplified_Prop_System_1.csv')
Nodes = int(System['Node Number'].max()) + 1
Elements = int(System['Element Number'].max()) + 1
FlowElements = Elements - 2

def view_results(filename):
    results = np.load(f'{filename}')
    t = results["t"]
    m_0 = results["m_0"]
    m_1 = results["m_1"]
    m_2 = results["m_2"]
    m_3 = results["m_3"]
    m_4 = results["m_4"]
    P = results["P"]
    m_dot = results["m_dot"]
    T = results["T"]

    # Create figures for each plot
    fig1 = plt.figure("Mass Flow Rate over Time")
    for i in range(0, FlowElements):
        label = 'm_dot_' + str(i+2)
        plt.plot(t,m_dot[:,i], label=label)
    plt.grid(which='major',axis='both',linewidth = 0.8)
    plt.minorticks_on()
    plt.grid(which='minor',axis='both',linewidth = 0.2)
    plt.xlabel('Time [s]')
    plt.ylabel('Mass Flow Rate [kg/s]')
    fig1.legend()

    fig2 = plt.figure("Temperature over Time")
    plt.plot(t,T, label='T')
    plt.grid(which='major',axis='both',linewidth = 0.8)
    plt.minorticks_on()
    plt.grid(which='minor',axis='both',linewidth = 0.2)
    plt.xlabel('Time [s]')
    plt.ylabel('Temperature [K]')
    fig2.legend()

    fig3 = plt.figure("Pressure over Time (Low Pressure)")
    for i in range(0, Nodes):
        label = 'P_' + str(i)
        plt.plot(t,P[:,i]*1e-5, label=label)
    plt.grid(which='major',axis='both',linewidth = 0.8)
    plt.minorticks_on()
    plt.grid(which='minor',axis='both',linewidth = 0.2)
    plt.xlabel('Time [s]')
    plt.ylabel('Pressure [bar]')
    plt.ylim(0,55)
    fig3.legend()

    fig4 = plt.figure("Pressure over Time (High Pressure)")
    for i in range(0, Nodes):
        label = 'P_' + str(i)
        plt.plot(t,P[:,i]*1e-5, label=label)
    plt.grid(which='major',axis='both',linewidth = 0.8)
    plt.minorticks_on()
    plt.grid(which='minor',axis='both',linewidth = 0.2)
    plt.xlabel('Time [s]')
    plt.ylabel('Pressure [bar]')
    plt.ylim(0,400)
    fig4.legend()

    fig5 = plt.figure("Mass over Time")
    plt.plot(t,m_0, label='m_0')
    plt.plot(t,m_1, label='m_1')
    plt.plot(t,m_2, label='m_2')
    plt.plot(t,m_3, label='m_3')
    plt.plot(t,m_4, label='m_4')
    plt.grid(which='major',axis='both',linewidth = 0.8)
    plt.minorticks_on()
    plt.grid(which='minor',axis='both',linewidth = 0.2)
    plt.xlabel('Time [s]')
    plt.ylabel('Mass [kg]')
    fig5.legend()

    fig6 = plt.figure("OF Ratio over Time")
    plt.plot(t,m_dot[:,3]/m_dot[:,4])
    plt.grid(which='major',axis='both',linewidth = 0.8)
    plt.minorticks_on()
    plt.grid(which='minor',axis='both',linewidth = 0.2)
    plt.xlabel('Time [s]')
    plt.ylabel('OF Ratio')

    # Show all figures
    plt.show()

if __name__ == "__main__":
    from sys import argv
    filename = argv[1]
    view_results(filename)
