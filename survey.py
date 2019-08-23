#survey
survey_questions = ["What's your name?", "Are you named after someone? If so, who?", "Apples or oranges?", "Dogs or cats?", "Would you rather fight one horse-sized duck or 20 duck-sized horses?", "Would you rather have a dog with human hands or a cat with a human face?", "What's your favorite dinner food?"]
survey_keys = ["name", "named_after", "app_or", "dog_cat", "duck_horse", "facecat", "dinner"]
total_ans = []
cont = True
import json

def main():
    while cont == True:
        print("Type 'BEGIN' to begin this survey.")
        initialize = input()
        if initialize.lower() == "begin":
            user_ans = {}
            for q in survey_questions:
                print(q)
                user_ans[q] = input()
            total_ans.append(user_ans)
            print("Thanks for your answers! :)")
            contvar = input("If you would like to continue collecting answers, type 'CONTINUE'. If you would like to end this program, type 'END'.\n")
            if contvar.lower() == "end":
                for z in range(10):
                    print()
                print("Thanks to everyone who answered this survey!")

                f = open("allanswers.json", "r")
                olddata = json.load(f)
                total_ans.extend(olddata)
                f.close()

                f.open("allanswers.json", "w")
                f.write('[\n')
                index = 0
                for t in total_ans:
                    if(index < len(total_ans)):
                        json.dump(t, f)
                        f.write("\n")
                    else:
                        json.dump(t, f)
                        f.write("\n")
                    index += 1

                f.write("]")
                f.close()
                cont == False
                break
            for y in range(3):
                print()

if __name__ == "__main__":
    main()
