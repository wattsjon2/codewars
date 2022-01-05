#Let us begin with an example:

#A man has a rather old car being worth $2000. He saw a secondhand car being worth $8000. He wants to keep his old car until he can buy the secondhand one.

#He thinks he can save $1000 each month but the prices of his old car and of the new one decrease of 1.5 percent per month. Furthermore this percent of loss increases of 0.5 percent at the end of every two months. Our man finds it difficult to make all these calculations.

#Can you help him?

#How many months will it take him to save up enough money to buy the car he wants, and how much money will he have left over?


def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    totalCash = 0
    monthCount = 1
    curValOld = startPriceOld
    curValNew = startPriceNew

    while totalCash + curValOld < curValNew:
        if monthCount % 2 == 0:
            percentLossByMonth += .5

        monthCount += 1

        curValNew = curValNew*(100 - percentLossByMonth)/100
        curValOld = curValOld*(100 - percentLossByMonth)/100
        totalCash += savingperMonth

    return [monthCount - 1, round(totalCash + curValOld - curValNew)]




print(nbMonths(2000, 8000, 1000, 1.5))
print(nbMonths(12000, 8000, 1000, 1.5))