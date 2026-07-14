quantity = int(input("quantity :"))
cost_price = int(input("cost_price :"))
sell_price = int(input("sell_price :"))
team_members = int(input("team_members :"))

total_cost = quantity * cost_price
total_income = sell_price * quantity
profit = total_cost - total_income
boss_income = 0.2 * total_income
member_income = (total_income - boss_income) / team_members

print(f"ต้นทุนทั้งหมด (บาท) = {total_cost}")
print(f"รายรับทั้งหมด (บาท) = {total_income}")
print(f"กำไรสุทธิ (บาท) = {profit}")
print(f"จำนวนเงินที่หักไปให้บอส (บาท) = {boss_income}")
print(f"จำนวนเงินที่ลูกน้องแต่ละคนได้ (บาท) = {member_income}")