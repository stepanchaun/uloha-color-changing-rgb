from PIL import Image

pic = Image.open('') #daval som tu fotku co mam ulozenu v pocitaci.

pic.show("Original")

conv = (
#   R  G  B  A  
    1, 0, 0, 0, # R = 1*R + 0*G + 0*B + 0*A
    0, 0, 0, 0, # G = 0*R + 1*G + 0*B + 0*A
    0, 0, 0, 0, # B = 0*R + 0*G + 1*B + 0*A
)

r = pic.convert('RGB', conv)
r.show('Red channel only')

conv = (
#   R  G  B  A  
    0, 0, 0, 0, # R = 1*R + 0*G + 0*B + 0*A
    0, 1, 0, 0, # G = 0*R + 1*G + 0*B + 0*A
    0, 0, 0, 0, # B = 0*R + 0*G + 1*B + 0*A
)

r = pic.convert('RGB', conv)
r.show('Green channel only')

conv = (
#   R  G  B  A  
    0, 0, 0, 0, # R = 1*R + 0*G + 0*B + 0*A
    0, 0, 0, 0, # G = 0*R + 1*G + 0*B + 0*A
    0, 0, 1, 0, # B = 0*R + 0*G + 1*B + 0*A
)

r = pic.convert('RGB', conv)
r.show('Blue channel only')
