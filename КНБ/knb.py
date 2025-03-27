import random
class Number:
	def ret(self):
		while True:
			chois = random.choice(['Камень', 'Ножницы', 'Бумага']).lower()
			inp = input('Введите значение: ')
			print(chois)
			if inp.lower() == chois:
				inpit = input('Ничья! Хочешь сыграть еще? y/n: ')
				if inpit == 'y':
					return self.ret()
				else:
					break			
			if (inp.lower() == 'ножницы' and chois == 'бумага') or (inp.lower() == 'бумага' and chois == 'камень') or (inp.lower() == 'камень' and chois == 'ножницы'):
				inpat = input('Ты победил! Хочешь сыграть еще? y/n: ')
				if inpat == 'y':
					return self.ret()
				else:
					break
			else:
				inpt = input('Ты проиграл! Хочешь сыграть еще? y/n: ')
				if inpt == 'y':
					return self.ret()
				else:
					break



obj = Number()

obj.ret()