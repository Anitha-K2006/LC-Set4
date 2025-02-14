int countDigits(int num) 
{
    int count=0,rem;
    int t=num;
    while(num!=0)
    {
        rem=num%10;
        if(t%rem==0)
        {
            count++;
        }
        num=num/10;
    }
    return count;
}
