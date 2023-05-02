# *******************************************
# Author: Tyler Jones (u3214218)
# Assessment: ST1 Capstone Project
# Date: 30/4/2023
# ********************************************
import tkinter as tk
from cvd_model import *

# Create window
class ChurnRate:
    def __init__(self):
        # Create the main window
        self.mainWindow = tk.Tk()
        self.mainWindow.title("Bank Customer Churn Rate")
        self.mainWindow.geometry("250x500")

        # Create frames
        self.frameOne = tk.Frame()
        self.frameTwo = tk.Frame()
        self.frameThree = tk.Frame()
        self.frameFour = tk.Frame()
        self.frameFive = tk.Frame()
        self.frameSix = tk.Frame()
        self.frameSeven = tk.Frame()
        self.frameEight = tk.Frame()
        self.frameNine = tk.Frame()
        self.frameTen = tk.Frame()
        self.frameEleven = tk.Frame()
        self.buttonFrame = tk.Frame()

        # Create and pack widgets

        # Frame one widgets
        self.creditScoreLabel = tk.Label(self.frameOne, text = "Enter credit score: ")
        self.creditScoreEntry = tk.Entry(self.frameOne, width = 15)
        self.creditScoreLabel.pack(side = "left")
        self.creditScoreEntry.pack(side = "left")
        self.frameOne.pack()

        # Frame two widgets
        self.countryLabel = tk.Label(self.frameTwo, text = "Enter country: ")
        self.countryVar = tk.StringVar()
        self.countryVar.set("France")
        self.countryInput = tk.OptionMenu(self.frameTwo, self.countryVar, "France", "Spain", "Germany")
        self.countryLabel.pack(side = "left")
        self.countryInput.pack(side = "left")
        self.frameTwo.pack()

        # Frame three widgets
        self.genderLabel = tk.Label(self.frameThree, text = "Enter gender: ")
        self.genderVar = tk.StringVar()
        self.genderVar.set("Male")
        self.genderInput = tk.OptionMenu(self.frameThree, self.genderVar, "Male", "Female")
        self.genderLabel.pack(side = "left")
        self.genderInput.pack(side = "left")
        self.frameThree.pack()

        # Frame four widgets
        self.ageLabel = tk.Label(self.frameFour, text = "Enter age: ")
        self.ageEntry = tk.Entry(self.frameFour, width = 15)
        self.ageLabel.pack(side = "left")
        self.ageEntry.pack(side = "left")
        self.frameFour.pack()

        # Frame five widgets
        self.tenureLabel = tk.Label(self.frameFive, text = "Enter tenure length: ")
        self.tenureEntry = tk.Entry(self.frameFive, width = 15)
        self.tenureLabel.pack(side = "left")
        self.tenureEntry.pack(side = "left")
        self.frameFive.pack()

        # Frame six widgets
        self.balanceLabel = tk.Label(self.frameSix, text = "Enter account balance: ")
        self.balanceEntry = tk.Entry(self.frameSix, width = 15)
        self.balanceLabel.pack(side = "left")
        self.balanceEntry.pack(side = "left")
        self.frameSix.pack()

        # Frame seven widgets
        self.productsNumberLabel = tk.Label(self.frameSeven, text = "Enter products amount: ")
        self.productsNumberEntry = tk.Entry(self.frameSeven, width = 15)
        self.productsNumberLabel.pack(side = "left")
        self.productsNumberEntry.pack(side = "left")
        self.frameSeven.pack()

        # Frame eight widgets
        self.creditCardLabel = tk.Label(self.frameEight, text = "Enter if credit card is owned: ")
        self.creditCardVar = tk.StringVar()
        self.creditCardVar.set("Yes")
        self.creditCardInput = tk.OptionMenu(self.frameEight, self.creditCardVar, "Yes", "No")
        self.creditCardLabel.pack(side = "left")
        self.creditCardInput.pack(side = "left")
        self.frameEight.pack()

        # Frame nine widgets
        self.activeMemberLabel = tk.Label(self.frameNine, text="Enter if active bank member: ")
        self.activeMemberVar = tk.StringVar()
        self.activeMemberVar.set("Yes")
        self.activeMemberInput = tk.OptionMenu(self.frameNine, self.activeMemberVar, "Yes", "No")
        self.activeMemberLabel.pack(side="left")
        self.activeMemberInput.pack(side="left")
        self.frameNine.pack()

        # Frame ten widgets
        self.estimatedSalaryLabel = tk.Label(self.frameTen, text="Enter estimated salary amount: ")
        self.estimatedSalaryEntry = tk.Entry(self.frameTen, width=15)
        self.estimatedSalaryLabel.pack(side="left")
        self.estimatedSalaryEntry.pack(side="left")
        self.frameTen.pack()

        # Creat button widgets
        self.churnButton = tk.Button(self.buttonFrame, text = "Button", command = self.ChurnItUp)
        self.quitButton = tk.Button(self.buttonFrame, text= "End", command=self.mainWindow.destroy)
        self.textBox = tk.Text(self.buttonFrame, bg = "light blue")
        self.churnButton.pack()
        self.quitButton.pack()
        self.textBox.pack()
        self.buttonFrame.pack()

        # Loop main window to keep open
        tk.mainloop( )

    def ChurnItUp(self):
        # Remove text from text box
        self.textBox.delete(1.0, tk.END)
        results = "Hello there. Hope you're having a wonderful day!"

        # Get credit score data
        creditScore = int(self.creditScoreEntry.get())

        # Get country data
        country = str(self.countryVar.get())
        if country == "France":
            country = 0
        elif country == "Spain":
            country = 1
        else:
            country = 2

        # Get gender data
        gender = str(self.genderVar.get())
        if gender == "Male":
            gender = 0
        else:
            gender = 1

        # Get age data
        age = int(self.ageEntry.get())

        # Get tenure data
        tenure = int(self.tenureEntry.get())

        # Get balance data
        balance = int(self.balanceEntry.get())

        # Get product number data
        productNumber = int(self.productsNumberEntry.get())

        # Get credit card data
        creditCard = str(self.creditCardVar.get())
        if creditCard == "Yes":
            creditCard = 1
        else:
            creditCard = 0


        # Get active member data
        activeMember = str(self.activeMemberVar.get())
        if activeMember == "Yes":
            activeMember = 1
        else:
            activeMember = 0

        # Get estimated salary data
        estimatedSalary = int(self.estimatedSalaryEntry.get())


        customerData = (creditScore, country, gender, age, tenure, balance, productNumber, creditCard, activeMember, estimatedSalary)
        churnRatePrediction = best_model.predict([customerData])
        disp_string = ("This prediction has an accuracy of:", str(model_accuracy))

        result = churnRatePrediction

        if (churnRatePrediction == [0]):
            results = (disp_string, '\n', "0 - You have never left the bank")
        else:
            results = (disp_string, '\n' + "1 - During some period you have left the bank")
            self.textBox.insert(1.0, results)

BankCustomerChurnRate = ChurnRate()