from threading import main_thread
import time


CORRECT_ANSWERS = ["C", "B","A","C","A","D","C","A","B","B"]

def collect_student_answers():
    collected_answers = []
    answer_bank = len(CORRECT_ANSWERS)
    for i in range(answer_bank):
        answer = input('Enter your answer for question {}: '.format(i+1)).upper()

        while not answer.isalpha():
            answer = input('Enter your answer for question {} (alphabetic): '.format(i+1)).upper()

        collected_answers.append(answer)

    return collected_answers


def check_answers(collected_answers):
    score = 0
    x=0
    for answer in collected_answers:
        if answer == CORRECT_ANSWERS[x]:
            score += 1
            x += 1
        else:
            x += 1
    return score

def main():
    print('Answer the following questions: ')
    print('1. What is the capital of Australia? \n A. Sydney \n B. Melbourne \nC. Canberra \nD. Perth \n 2. Who developed the theory of relativity?\n A. Isaac Newton \nB. Albert Einstein \nC. Galileo Galilei \nD. Marie Curie \n 3. Which planet is known as the "Gas Giant"? \nA. Jupiter \nB. Saturn \nC. Mars \nD. Venus \n 4. What is the chemical symbol for oxygen? \nA. O2 \nB. CO2 \nC. O \nD. H2O \n 5. In which year did World War II end? \nA. 1945 \nB. 1918 \nC. 1939 \nD. 1955 \n 6. What is the largest ocean on Earth? \nA. Atlantic Ocean \nB. Indian Ocean \nC. Arctic Ocean \nD. Pacific Ocean \n 7. Who painted the Mona Lisa?\n A. Vincent van Gogh\n B. Pablo Picasso \nC. Leonardo da Vinci \nD. Claude Monet \n 8. Which element has the atomic number 79?\n A. Gold \nB. Silver\n C. Copper \nD. Platinum \n 9. What is the square root of 144?\n A. 11 \nB. 12\n C. 13\n D. 14 \n 10. Who wrote "To Kill a Mockingbird"? \nA. J.K. Rowling \nB. Harper Lee\n C. Ernest Hemingway\n D. F. Scott Fitzgerald')
    time.sleep(5)
    score=check_answers(collect_student_answers())
    print('Your score is {} out of 10'.format(score))
main()