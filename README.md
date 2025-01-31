                                                                 --Basic Keylogger--
                                                          (For educational purposes only)

1. What is a keylogger?
- A computer program that records every keystroke made by a computer user, especially in order to gain fraudulent access to passwords and other confidential information. (google)

2. What is the use of a keylogger in cybersecurity?
- Keyloggers in cybersecurity are used for ethical purposes like penetration testing, monitoring insider threats, and investigating breaches. They help detect data theft, improve security awareness, and monitor remote workers.

3. My experience while developing it: 
    i. I was browsing the web for ideas on a project when I landed upon keylogger. It was beginner-friendly enough for me to try. I looked online on other people's code 
            and tried to find my own way of doing it that fitted the ideas I had for a keylogger(like encryption and free real time message delivery)

    ii. I used pynput library to get the keyboard inputs and printed them out on a file first. It worked fine and printed my keystrokes down with a little to no error.

   iii. Then I moved on to integrating encryption on it ever if the person ever opens the file by mistake, they would not get creeped out and delete the file before it 
             has served its purpose. I used Fernet library for encryption. After generating a key, everything was encrypted. At first, I was printing out a file with the 
             normal inputs of the keystrokes and another one to store the encrypted version of it, which failed the reason I was encrypting it all in the first place, so I 
             brainstormed for a while and added real time encryption as the user entered his keystrokes.

    iv. Then I moved on to which way I would receive my data, gmail or google drive wouldn't suffice for the level of privacy I wanted. I ended up creating a Telegram bot 
            using @botfather and used its token and chatid to integrate it all in my code.

    v. I imported some libraries to facilate the schedule of texts to not get notifications every second about everyone single word individually, so I set a timer which 
           can easily altered (perferably 5 or 10 minutes). There would've also been a storage issue if I had used gmail instead of telegram bot here.

     vi. Later I realised that my token, chat id and encryption were lying out in open, if ever in case my program got caught I would be traced back to. So, I made 
            different .key files for the details that shouldn't be in the open for the taking.

    vii. At this point, I found it weird that I was receiving encrypted messages over telegram which I had to run through another code that was decrypting it. So, I added 
             real time decryption as it extracted data from the file and delivered it to telegram. I still do not know if it harms the integrity of the program but I believe 
             it doesn't.

     viii. I added some troubleshooting messages just in case I had to check if everything was working alright or not.

     ix. I was all finished with my keylogger by that point. I made some quality of life changes here and there but they're not worthy of mention (like function and 
            variable name changes, etc). This project was only made to test my skills and get further knowledge in the field of cybersecurity. NOT FOR ANY MALICIOUS USE.

4. How to use:
     i. keylogger.py is the main code you can use to create the keylogger in any device, all you have to do is connect your telegram bot token and its chat id by a .key               file.

     ii. stopper.py is a code I created to find if any kind of keylogger using some common libraries are running (like pypnut, cryptography, etc)

    iii. FILES THAT NEED TO BE CREATED: "telegram.key" just copy paste telegram bot token here without any alteration and "chatid.key" copy paste the chatid you'd find 
        when you text the bot.

Thank You for reading through my decription of the project.

