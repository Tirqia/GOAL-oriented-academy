# def isValidCoupon(couponCode, totalAmount):
#     return (couponCode == "SALE" or couponCode == "BIGSALE") and totalAmount >= 50 or couponCode == "LILSALE"


def isValidCoupon(couponCode, totalAmount):
    if (couponCode == "SALE" or couponCode == "BIGSALE") and totalAmount >= 50:
        return True
    elif couponCode == "LILSALE":
        return True
    else:
        return False


print(isValidCoupon("SALE", 68))
print(isValidCoupon("BIGSALE", 17))
print(isValidCoupon("LILSALE", 4))

'''
ფუნქცია isValidCoupon ამოწმებს ორ ძირითად პირობას:
თუ კუპონის კოდი არის "Sale" ან "BIGSALE", და totalAmount არის 50-ზე მეტი ან ტოლი, ის აბრუნებს True-ს.
თუ კუპონის კოდი არის "LILSALE", ის აბრუნებს True-ს, მიუხედავად totalAmount-ისა.
თუ არცერთი ეს პირობა არ არის დაკმაყოფილებული, ფუნქცია აბრუნებს False-ს.
ფუნქციის ეს ვერსია იყენებს if-elif-else სტრუქტურას, რათა მკაფიოდ გამოიკვეთოს თითოეული მდგომარეობა და დააბრუნოს შესაბამისი ლოგიკური მნიშვნელობა შეყვანის პარამეტრებზე დაყრდნობით.
'''
