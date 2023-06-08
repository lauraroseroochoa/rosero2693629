def bookRequest(self,title):
        if title in self.title:
            if Book.reservationStatus(self, title)=='disponible':
                print('libro disponible para reservarlo')
                print('1: reservar')
                print('2: no reservar')
                selector= input('ingresa una opcion')
                match selector:
                    case'1':
                        self.status = 'reservado'
                            return self.status
                    case'2':
                            return 'no reservado'
                