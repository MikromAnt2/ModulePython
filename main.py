from trans import gtranslator
import asyncio
import os

async def main():
    if os.path.exists("MyData.txt"):
        try:
            with open("MyData.txt", "r", encoding="UTF-8") as f:
                content = f.read()
            print(content)
            return
        except Exception as e:
            print(f"Error: {e}")
            return

    experience = input("Enter your experience(years): ")
    salary = input("Enter your salary(uah): ")
    language = input("Enter language of file: ")
    result = salaryBonus(experience, salary)
    if result is None:
        print("Error calculating bonus.")
        return
    bonus, bonusPercent, totalSalary = result

    try:
        experienceTranslated = await gtranslator.TransLate("Experience", "auto", language)
        salaryTranslated = await gtranslator.TransLate("Salary", "auto", language)
        bonusPercentTranslated = await gtranslator.TransLate("Bonus(%)", "auto", language)
        bonusUahTranslated = await gtranslator.TransLate("Bonus(uah)", "auto", language)
        totalTranslated = await gtranslator.TransLate("Total", "auto", language)

        languageName= await gtranslator.CodeLang(language)
        
        with open("MyData.txt", "w", encoding="UTF-8") as f:
            f.write(f"Language: {languageName}\n")
            f.write(f"{experienceTranslated}: {experience}\n")
            f.write(f"{salaryTranslated}: {salary}\n")
            f.write(f"{bonusPercentTranslated}: {bonusPercent}\n")
            f.write(f"{bonusUahTranslated}: {bonus}\n")
            f.write(f"{totalTranslated}: {totalSalary}\n")
        
        print(f"Data written to file MyData.txt with language {language}")
        print(f"Language: {languageName}")
        
    except Exception as e:
        print(f"Error: {e}")
        return

def salaryBonus(expirience, salary):
    try:
        exp = float(expirience)
        sal = float(salary)
        if exp < 0 or exp > 70:
            print("Expirience must be from 0 to 70 years")
            return
        if sal < 0:
            print("Salary must be > 0")
            return
        bonusPercent = 0
        if 2 <= exp < 5:
            bonusPercent = 2
        elif 5 <= exp < 10:
            bonusPercent = 5
        elif exp >= 10:
            bonusPercent = 10
        bonus = sal * bonusPercent / 100
        totalSalary = sal + bonus

        return bonus, bonusPercent, totalSalary
    except Exception as e:
        print(f"Error: {e}")
        return

if __name__ == "__main__":
    asyncio.run(main())