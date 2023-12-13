import pandas as pd
import matplotlib.pyplot as plt

X = 6
Y = 19

# https://chat.openai.com/share/543d2edd-a96f-46f8-ad4c-bdda7328e519

def creaza_graf(titlu, data):
    durata = data['Durata']
    puls = data['Puls']
    max_puls = data['MaxPuls']
    calorii = data['Calorii']

    fig, axs = plt.subplots(2, 2, figsize=(10, 8)) #grid de 4 grafice cu size

    axs[0, 0].plot(durata, label='Durata', color='red', marker='o') #marker pt puncte pe grafic
    axs[0, 0].set_title('Durata')

    axs[0, 1].plot(puls, label='Puls', color='blue', marker='o')
    axs[0, 1].set_title('Puls')

    axs[1, 0].plot(max_puls, label='MaxPuls', color='green', marker='o')
    axs[1, 0].set_title('MaxPuls')

    axs[1, 1].plot(calorii, label='Calorii', color='purple', marker='o')
    axs[1, 1].set_title('Calorii')

    plt.suptitle(titlu)
   # plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    data = pd.read_csv('data.csv')
    creaza_graf('Afiseaza tot', data)

    data = pd.read_csv('data.csv', nrows=X) # primele x valori
    creaza_graf('Primele ' + str(X) + ' valori', data)

    data = pd.read_csv('data.csv').tail(Y) # ultiele y valori
    creaza_graf('Ultimele ' + str(Y) + ' valori', data)