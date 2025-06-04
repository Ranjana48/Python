# WAP to convert currency RS. to Dollor and vise versa.

# method-1
dollor = int(input("Enter dollor: "))
Rs = dollor*85
print(f'Dollor = {dollor} and Rupees = {Rs}')
Rupees = int(input("Enter rupees : "))
dollor1 = float(Rupees/85)
print(f'Rs is : {Rupees} and Dollor is : {dollor1:.2f}')
   
   
   
# method-2
Amount = int(input("Enter Amount : "))
rs = Amount*85
dollor = Amount/85
print(f'''
      Entered Amount is : {Amount} convert into rupees = {rs}
      Entered Amount is : {Amount} convered into dollor = {dollor}
      
      ''')