command_name = 'commandfile'
command = ''

if command == '':
	command = input('Enter the command: ')

# up, down, north, south, west, east
facing = 'up'
wool_types = [
	"white_wool",
	"orange_wool",
	"magenta_wool",
	"light_blue_wool",
	"yellow_wool",
	"lime_wool",
	"pink_wool",
	"gray_wool",
	"light_gray_wool",
	"cyan_wool",
	"purple_wool",
	"blue_wool",
	"brown_wool",
	"green_wool",
	"red_wool",
	"black_wool"
]
shulker_types = [
	"white_shulker_box",
	"orange_shulker_box",
	"magenta_shulker_box",
	"light_blue_shulker_box",
	"yellow_shulker_box",
	"lime_shulker_box",
	"pink_shulker_box",
	"gray_shulker_box",
	"light_gray_shulker_box",
	"cyan_shulker_box",
	"purple_shulker_box",
	"blue_shulker_box",
	"brown_shulker_box",
	"green_shulker_box",
	"red_shulker_box",
	"black_shulker_box"
]
for i in range(len(wool_types)):
    
    command = command.replace(wool_types[i], f'{shulker_types[i]}[facing={facing}]')
#create a txt file with the command
with open(f'{command_name}.txt', 'w') as f:
    f.write(command)
print(f'Command has been written to {command_name}.txt')

#print(command)
