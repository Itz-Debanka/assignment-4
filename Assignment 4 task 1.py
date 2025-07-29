try:
   file1=open('sample.txt',"r")

   line=file1.readlines()

   a=0
   for i in line:
      a=a+1
      print( "line ",a,": ",i)



   file1.close()
except:
   print('Error: The file sample.txt was not found')
