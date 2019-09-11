def Draw_line(tick_length, tick_label=''):
	line = '-' * tick_length
	if tick_label:
		line += ' ' + tick_label
	print(line)

def Draw_interval(center_length):
	if center_length > 0:
		Draw_interval(center_length - 1)
		Draw_line(center_length)
		Draw_interval(center_length - 1)
def Draw_ruler(num_inches, major_length):
	Draw_line(major_length, '0')
	for j in range(1,1 + num_inches):
		Draw_interval(major_length - 1)
		Draw_line(major_length, str(j))

Draw_ruler(2, 2)
