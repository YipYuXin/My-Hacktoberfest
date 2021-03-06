print("Title of program: Post Exam Activity bot")
print()
while True:
  description = input("Could you describe how you feel after the examinations?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("Keep smiling. Life is good!")
      counter += 1
    if each_word == "bored":
      feelings_list.append("bored")
      encouragement_list.append("Find something fun to do")
      counter += 1
    if each_word == "tiring":
      feelings_list.append("tiring")
      encouragement_list.append("Get some sleep")
      counter += 1
    if each_word == "relieved":
      feelings_list.append("relieved")
      encouragement_list.append("Relax after the stressful examinations")
      counter += 1

    if each_word == "dead tired":
      feelings_list.append("dead tired")
      encouragement_list.append("Just find something fun to do")
      counter += 1
      
     if each_word == "sad":
      feelings_list.append("sad")
      encouragement_list.append("talk to your friends")
      counter += 1    

     if each_word == "anger":
      feelings_list.append("anger")
      encouragement_list.append("Take a deep breath and count to three, try to think of something that is positive!")
      counter += 1 
      
     if each_word == "surprise":
      feelings_list.append("surprise")
      encouragement_list.append("Good for you!")

     if each_word == "worried":
      feelings_list.append("worried")
      encouragement_list.append("everything is going to be fine")
      counter += 1
      
     if each_word == "anticipating":
      feelings_list.append("anticipating")
      encouragement_list.append("wishing you all the best with the results!")
      counter += 1
      
    if each_word == "scared":
      feelings_list.append("scared")
      encouragement_list.append("it's okay, everything is going to be fine")
      counter += 1
      
    if each_word == "doomed":
      feelings_list.append("doomed")
      encouragement_list.append("It's alright, it'll not be that bad. There's always a next time too!")
      counter += 1
    
    if each_word == "disappointed":
      feelings_list.append("disappointed")
      encouragement_list.append("Don't worry! Everyone is bound to face failures in the course of their lives, what is most important is you that pick yourself up and never give up!")
      counter += 1
    
    if each_word == "frustrated":
      feelings_list.append("frustrated")
      encouragement_list.append("What are you frustrated about? Maybe you can try telling someone? They may be able to come up with different perspectives that can help you!")
      counter += 1
      
    if counter == 0:

      output = "Sorry I don't really understand. Please use different words?"

  elif counter == 1:
    
      output = "It seems that you are feeling quite " + feelings_list[0] + ". However, do remember to "+ encouragement_list[0] + "! Hope you feel better :)"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()
  
