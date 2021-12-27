//In this kata you are required to, given a string, replace every letter with its position in the alphabet.

//If anything in the text isn't a letter, ignore it and don't return it.

//alphabetPosition("The sunset sets at twelve o' clock.")

//Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)

function alphabetPosition(text) {
    let num_string = ""
    let letter_dict = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
    for (let i = 0; i < text.length; i++){
        if (letter_dict.hasOwnProperty(text[i].toLowerCase()) == true){
            num_string += " " + letter_dict[text[i].toLowerCase()]
            console.log(i)
        }
    }

    return num_string.trim()
}

console.log(alphabetPosition(" The sunset sets at twelve o' clock."))