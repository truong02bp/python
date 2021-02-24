#include <stdio.h>
#include <stdlib.h>
int main()
{
   int n,a[100],minn;
   FILE *fptr;

   fptr = fopen("input.txt","r");
 
   if(fptr == NULL)
   {
      printf("Error!");   
      exit(1);             
   }
   fscanf(fptr,"%d",&n);
   printf("%d",n); 
   for (int i=0;i<n;i++)
       fscanf(fptr,"%d",&a[i]);  
    minn = a[0];
    for (int i=1;i<n;i++)
        if (a[i] < minn)
            minn = a[i];
    printf("%d",minn);        
   fclose(fptr);
   return 0;
}