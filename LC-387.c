int firstUniqChar(char* s) 
{
    
    for(int i=0;s[i]!='\0';i++)
    {
        int t=1;
       for(int j=0;s[j]!='\0';j++)
       {
          if(s[i]==s[j]&&i!=j)
          {
            t=0;
            break;
          }
       }
       if(t==1)
       {
        return i;
        break;
       }
    }
    return -1;
}
