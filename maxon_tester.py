from maxon import Maxon


def main():
    try:
        maxon = Maxon()
        try:
            config_file = maxon.select_config()
            maxon.load_config(config_file)
        except ValueError as err:
            print(err)
            m = input('¿Definir parametros maualmente? (s/N):') or 'N'
            if m == 's' or m == 'S':
                maxon.manual_parameters()
            else:
                exit(0)
        maxon.start_sender()
        while True:
            maxon.menu()

    except ValueError as err:
        print(err)
    except KeyboardInterrupt:
        print('Keyboard interrupt')


if __name__ == '__main__':
    main()
