'''A recipe you are reading states how many grams you need for the ingredient.Unfortunately, your store only sells items in ounces.
Create a function to convert grams to ounces.
ounces = 28.3495231 * grams'''
def to_ounces(grams):
    ounces=grams*28.3495231
    return ounces
grams=100
r=to_ounces(grams)
print(f"{r:.2f}ounces")