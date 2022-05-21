import json
import numpy as np
import os
from colorsys import rgb_to_hsv

# Export gradient
def saveToFile(velocities, filename="exports/output"):
	for i in range(17 - len(velocities)):
		# velocities.append(127)
		pass

	with open(filename, mode="w") as file:
		for i, vel in enumerate(velocities):
			print(f"{i}, {vel};", file=file)

# Import gradient from file
def readJson(fileName="gradients.json"):
	with open(fileName) as json_file:
		data = json.load(json_file)
	return data

# Get R, G and B values from string hex code
def hexToRgb(hexCode):
	hexCode = hexCode[1:]
	r = int(hexCode[:2], 16)
	g = int(hexCode[2:4], 16)
	b = int(hexCode[4:], 16)
	return r, g, b

# get list of gradient colors
def getGradient(colors, samples=8):
	gradient = []
	times = len(colors) - 1

	for i in range(times):
		col1 = np.array(colors[i])
		col2 = np.array(colors[i + 1])
		colD = (col2 - col1) / ((samples - 1) // times)

		for num in range(samples // times):
			gradient.append(list(col1 + colD * num))
	return gradient

# read all colors from given palette
def get_palette(filename="palette"):
	palette = {}

	with open(filename) as file:
		for line in file.readlines():
			palette[int(line.split(", ")[0])] = \
			eval("(" + line.split(", ")[1].
				replace(";", "").replace(" ", ", ").replace("\n", "") + ")")
	return palette

# get closets color to given using rgb distance
def closest_color(rgb, palette):

	if len(rgb) == 3:
		r, g, b = rgb
	else:
		r, g, b, a = rgb

	color_diffs = []
	for color in palette.values():
		cr, cg, cb = color
		color_diff = ((r / 4 - cr)**2 + (g / 4 - cg)**2 + (b / 4 - cb)**2)**0.5
		color_diffs.append((color_diff, color))

	color = min(color_diffs)[1]
	return color, list(palette.keys())[list(palette.values()).index(color)]

# get closets color to given using hsv distance
def closest_color_hsv(rgb, palette):
	if len(rgb) == 3:
		r, g, b = rgb
	else:
		r, g, b, a = rgb

	h, s, v = rgb_to_hsv(r / 255, g / 255, b / 255)

	color_diffs = []
	for color in palette.values():
		cr, cg, cb = color
		ch, cs, cv = rgb_to_hsv(cr / 255, cg / 255, cb / 255)

		color_diff = ((h - ch)**2 * 0.475 + (s - cs)**2 * 0.2875 + (v - cv)**2 * 0.2375)**0.5
		color_diffs.append((color_diff, color))

	color = min(color_diffs)[1]
	return color, list(palette.keys())[list(palette.values()).index(color)]

palette = get_palette("palette")
for l in range(2, 17):
	length = l # Length of every gradient
	path = f"gradients/len{l}/" # Relative folder to store files at.

	if not os.path.exists(path):
		# Create a new directory because it does not exist
		os.makedirs(path)

	# Go through all gradients in json
	for item in readJson():
		name, colors = item["name"], item["colors"]

		# Create list for this gradient. Also, convert all hex codes from .json to rgb tuple
		gradient = getGradient([hexToRgb(hexCode) for hexCode in colors], length)

		# Output midi velocities
		velocities = []

		# Get velocities for all colors ([0] - rgb color, [1] - velocity)
		for col in gradient:
			velocities.append(closest_color_hsv(col, palette)[1])

		# Save velocity scheme to file
		saveToFile(velocities, path + name.lower())
