
import turtle
def main():
	window = turtle.Screen()
	t = turtle.Turtle()
	make_square(t)
	turtle.mainloop()


def make_square(t):
	length = int(input("Tamaño:"))

	for i in range(3):
		make_line_and_turn(t,length)

	make_line_and_turn(t,length)

def make_line_and_turn(t,length):
	t.forward(length)
	t.left(90)	

if __name__ == '__main__':
	main()
