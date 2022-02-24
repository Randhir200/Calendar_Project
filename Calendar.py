T=int(input())
days=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
for i in range(T):
    date=input()
    slas1=date.index("/")
    slas2=date.index("/", 3, 8)    
    day=int(date[:slas1])
    month=int(date[slas1+1:slas2])
    year=int(date[slas2+1:])
    # it's for counting odd days
    odddays=0
    # function for calculate odd days for decade
    def odInDecade(decade):
        lp   = decade//4
        ordy = decade-lp
        return lp*2+ordy*1
    
    y=year-1
    # counter for decreasing month value by one
    c = month-1
    # I need only those years thats just come after multiple of 400 thats why i do modulus by 400  
    a=y%400
    
    #check how much remaining years to calculate for odd days 
    if a>=300:
        # since there is more than 300 years so increase odddays value by one
        odddays +=1
        if a%100!=0:
            # now i have calculate odd odddays for rest decate part
            decade=a%100
            # I used function because whatever i write in function it'll use in miltiple time
            odddays=odddays+odInDecade(decade)
    elif a>=200:
        odddays +=3
        if a%100!=0:
            decade=a%100
            odddays=odddays+odInDecade(decade)
    elif a>=100:
        odddays +=5
        if a%100!=0:
            decade=a%100
            odddays=odddays+odInDecade(decade)
    elif y<=100:
        odddays +=5
        if a%100!=0:
            decade=y
            odddays=odddays+odInDecade(decade)
    else:
        odddays=odddays+odInDecade(a)

        # odddays calculating for the months
    for k in range(month-1):
                    if c in [1,3,5,7,8,10]:
                        odddays+=3
                    elif c in [4,6,9,11]:
                        odddays+=2
                    elif year%100!=0 and year%4==0:  
                           if c==2:
                              odddays+=1    
                    elif year%100==0 and year%400==0:    
                           if c==2:
                              odddays+=1
                    c-=1
    # odd days calculating for days  
    odddays=odddays+day
    # now calculating exact odddays
    odddays=odddays%7
    
    # this loop for showing day according to odddays
    for i in range(len(days)):
        if odddays==i:
           print(days[i])
        
     
