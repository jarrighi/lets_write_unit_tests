import cmd
import requests

class Pokemon(object):
	def __init__(self, data):
		self.name = data['name']
		self.id = data['id']
		self.types = [t['type']['name'] for t in data['types']]

	def __str__(self):
		return 'Pokemon #{}: {}'.format(self.id, self.name)

class Pokedex(cmd.Cmd):
	intro = 'Welcome to the PokeDex. Type help for a list of commands.\n'
	prompt = '\n> '
	collection = {}

	def do_catch(self, arg):
		'Add a pokemon to the collection'
		if arg in self.collection: 
			print('{} is already in your collection'.format(arg))
		else:
			r = requests.get('http://pokeapi.co/api/v2/pokemon/{}'.format(arg))
			data = r.json()
			new = Pokemon(data)
			self.collection[arg] = new
			print('Caught pokemon {}'.format(arg))

	def do_lookup(self, arg):
		'Find a pokemon from the collection by name'
		# Look in the collection
		if not arg in self.collection:
			print("You haven't caught {} yet".format(arg))
		else:
			print(self.collection[arg])
	
	def do_print_collection(self, arg):
		'Print a list of the pokemon in your collection'
		for key in self.collection.keys():
			print(key)

	# def do_list(self, arg):
	# 	'Print a list of the given resource'
	# 	# Get a list from the API
	# 	pass

	def do_quit(self, arg):
		'Exit the PokeDex'
		return True

if __name__ == "__main__": 
	Pokedex().cmdloop()