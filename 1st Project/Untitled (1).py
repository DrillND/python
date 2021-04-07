#!/usr/bin/env python
# coding: utf-8

# In[16]:


print(h)

print(h[-1])


# In[15]:


c='life'
d='is'
e='too'
f='short'
g= ' '
h = c+g+d+g+e+g+f
len(h)

print(h[0]+e[1]+'v'+c[3])


# In[19]:


print(h[-4]+h[-3]+h[-2]+h[-5]+h[3])
print(h)
print(h[12:])


# In[55]:


td = "20210407맑음"
g= ' '
print(td[0:4]+'년' +g+ td[4:6]+'월' +g+td[6:8]+'일'+g+td[-2:])

#td.replace('2','3')


# In[180]:


# 원하는 구절 찾기
# 요구사항 1. 방탄소년단 전체가사를 사용해주세요.
# 요구사항 2. "I'm diamond you know I glow up" 이 구절만 출력해주세요.
# 요구사항 3. a.find("I'm diamond")
# 요구사항 4. zip파일 - .ipnyb 파일을 압축해서 올리기
bts = '''
Jump up to the top LeBron
Ding dong call me on my phone
Ice tea and a game of ping pong
This is getting heavy
Can you hear the bass boom, I'm ready
Life is sweet as honey
Yeah this beat cha ching like money
Disco overload I'm into that I'm good to go
I'm diamond you know I glow up
Hey, so let's go
Cos ah ah I'm in the stars tonight
So watch me bring the fire and set the night alight
Shining through the city with a little funk and soul
So I'mma light it up like dynamite, woah
Bring a friend join the crowd
Whoever wanna come along
Word up talk the talk just move like we off the wall
Day or night the sky's alight
So we dance to the break of dawn
Ladies and gentlemen,
I got the medicine so you should keep ya eyes on the ball, huh
This is getting heavy
Can you hear the bass boom, I'm ready
Life is sweet as honey
Yeah this beat cha ching like money
Disco overload I'm into that I'm good to go
I'm diamond you know I glow up
Let's go
Cos ah ah I'm in the stars tonight
So watch me bring the fire and set the night alight
Shining through the city with a little funk and soul
So I'mma light it up like dynamite, woah
Dynnnnnanana, life is dynamite
Dynnnnnanana, life is dynamite
Shining through the city with a little funk and soul
So I'mma light it up like dynamite, woah
Dynnnnnanana eh
Dynnnnnanana eh
Dynnnnnanana eh
Light it up like dynamite
Dynnnnnanana eh
Dynnnnnanana eh
Dynnnnnanana eh
Light it up like dynamite
Cos ah ah I'm in the stars tonight
So watch me bring the fire and set the night alight
Shining through the city with a little funk and soul
So I'mma light it up like dynamite
Cos ah ah I'm in the stars tonight
So watch me bring the fire and set the night alight
Shining through the city with a little funk and soul
So I'mma light it up like dynamite, woah
Dynnnnnanana, life is dynamite
Dynnnnnanana, life is dynamite
Shining through the city with a little funk and soul
So I'mma light it up like dynamite, woah
'''

a= bts.find("I'm diamond you know I glow up")
b= len("I'm diamond you know I glow up")
print(bts[a:a+b])

bts.find("Day")
b=a[823:]
brint(b)
c=b.split('\n')
print(c[0])


# In[109]:


rose = '''
My life's been magic, seems fantastic
I used to have a hole in the wall with a mattress
Funny when you want it, suddenly you have it
You find out that your gold's just plastic
Every day, every night
I've been thinkin' back on you and I
Every day, every night
I worked my whole life
Just to get right, just to be like
"Look at me, I'm never coming down"
I worked my whole life
Just to get high, just to realize
Everything I need is on the
Everything I need is on the ground
On the ground
Everything I need is on the ground
(Nah, but they don't hear me though)
(Yeah, what goes up must come down)
(Nah, but they don't hear me though)
(You're runnin' out of time)
My world's been hectic, seems electric
But I've been waking up with your voice in my head
And I'm tryna send a message and let you know that
Every single minute I'm without you, I regret it
Every day, every night
I've been thinkin' back on you and I
Every day, every night
I worked my whole life
Just to get right, just to be like
"Look at me, I'm never coming down"
I worked my whole life
Just to get high, just to realize
Everything I need is on the
Everything I need is on the ground
On the ground
Everything I need is on the ground
(Nah, but they don't hear me though)
(Yeah, what goes up must come down)
(Nah, but they don't hear me though)
(You're runnin' out of time)
I'm way up in the clouds
And they say I've made it now
But I figured it out
Everything I need is on the ground (yeah, yeah)
Just drove by your house (just drove by your house)
So far from you now (so far from you now)
But I figured it out
Everything I need is on the
Everything I need is on the ground
On the ground
Everything I need is on the ground
(Nah, but they don't hear me though)
On the ground
(Nah, but they don't hear me though)
Everything I need is on the ground
'''
#a=rose.find("On the ground")
b=rose.split("On the ground")
#a=rose.count("On the ground")
print(b)


# In[91]:


a= '''life is too short\nyou need python'''
s=a.split('\n')
print(s[0])


# In[143]:


rose = '''
My life's been magic, seems fantastic
I used to have a hole in the wall with a mattress
Funny when you want it, suddenly you have it
You find out that your gold's just plastic
Every day, every night
I've been thinkin' back on you and I
Every day, every night
I worked my whole life
Just to get right, just to be like
"Look at me, I'm never coming down"
I worked my whole life
Just to get high, just to realize
Everything I need is on the
Everything I need is on the ground
On the ground
Everything I need is on the ground
(Nah, but they don't hear me though)
(Yeah, what goes up must come down)
(Nah, but they don't hear me though)
(You're runnin' out of time)
My world's been hectic, seems electric
But I've been waking up with your voice in my head
And I'm tryna send a message and let you know that
Every single minute I'm without you, I regret it
Every day, every night
I've been thinkin' back on you and I
Every day, every night
I worked my whole life
Just to get right, just to be like
"Look at me, I'm never coming down"
I worked my whole life
Just to get high, just to realize
Everything I need is on the
Everything I need is on the ground
On the ground
Everything I need is on the ground
(Nah, but they don't hear me though)
(Yeah, what goes up must come down)
(Nah, but they don't hear me though)
(You're runnin' out of time)
I'm way up in the clouds
And they say I've made it now
But I figured it out
Everything I need is on the ground (yeah, yeah)
Just drove by your house (just drove by your house)
So far from you now (so far from you now)
But I figured it out
Everything I need is on the
Everything I need is on the ground
On the ground
Everything I need is on the ground
(Nah, but they don't hear me though)
On the ground
(Nah, but they don't hear me though)
Everything I need is on the ground
'''
t=rose.split('\n')
a=t[15]
#b=rose.find('On the ground')
#a=rose.split('On the ground')
print(a)


# In[212]:


rose = '''
My life's been magic, seems fantastic
I used to have a hole in the wall with a mattress
Funny when you want it, suddenly you have it
You find out that your gold's just plastic
Every day, every night
I've been thinkin' back on you and I
Every day, every night
I worked my whole life
Just to get right, just to be like
"Look at me, I'm never coming down"
I worked my whole life
Just to get high, just to realize
Everything I need is on the
Everything I need is on the ground
On the ground
Everything I need is on the ground
(Nah, but they don't hear me though)
(Yeah, what goes up must come down)
(Nah, but they don't hear me though)
(You're runnin' out of time)
My world's been hectic, seems electric
But I've been waking up with your voice in my head
And I'm tryna send a message and let you know that
Every single minute I'm without you, I regret it
Every day, every night
I've been thinkin' back on you and I
Every day, every night
I worked my whole life
Just to get right, just to be like
"Look at me, I'm never coming down"
I worked my whole life
Just to get high, just to realize
Everything I need is on the
Everything I need is on the ground
On the ground
Everything I need is on the ground
(Nah, but they don't hear me though)
(Yeah, what goes up must come down)
(Nah, but they don't hear me though)
(You're runnin' out of time)
I'm way up in the clouds
And they say I've made it now
But I figured it out
Everything I need is on the ground (yeah, yeah)
Just drove by your house (just drove by your house)
So far from you now (so far from you now)
But I figured it out
Everything I need is on the
Everything I need is on the ground
On the ground
Everything I need is on the ground
(Nah, but they don't hear me though)
On the ground
(Nah, but they don't hear me though)
Everything I need is on the ground
'''
#17

a=rose.replace("\n"," ")
b=a.split(" ")

#for (i in b i=="on" or i=="On"  count += 1)
c=b.count('on')
d=b.count('On')

print(c+d)


# In[204]:


a=3
if a%2==0:
    print("짝수")
else:
    print("홀수")


# In[215]:


x==7
#5<x or x<10
#5<x and x>10
5<x and not x >10


# In[ ]:




