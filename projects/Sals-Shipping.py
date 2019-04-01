#Write a program that asks the user for the weight of their package and then tells them which method of shipping is
# cheapest and how much it will cost to ship their package using Sal's Shippers.

#Finding the cheapest shipping method

#ground shipping costs
ground_shipping_flat_charge = 20.00
premium_ground_shipping_rate = 125.00
twolb_price_per_pound = 1.50
threelb_to_sixlb_price_per_pound = 3.00
sevenlb_to_tenlb_price_per_pound = 4.00
elevenlb_or_greater = 4.75

#drone dhipping costs
ds_twolb_price_per_pound = 4.50
ds_threelb_to_sixlb_price_per_pound = 9.00
ds_sevenlb_to_tenlb_price_per_pound = 12.00
ds_elevenlb_or_greater = 14.25

#calculate the price for ground shipping
def price_for_ground_shipping(weight):
        if weight <= 2:
            gs_cost = (twolb_price_per_pound * weight) + ground_shipping_flat_charge
        elif (weight > 2) and (weight < 7):
            gs_cost = (threelb_to_sixlb_price_per_pound *weight) + ground_shipping_flat_charge
        elif (weight > 6) and (weight < 11):
            gs_cost = (sevenlb_to_tenlb_price_per_pound * weight) + ground_shipping_flat_charge
        elif weight >=11:
            gs_cost = (elevenlb_or_greater * weight) + ground_shipping_flat_charge
        return gs_cost
print(price_for_ground_shipping(48))

#calculate the price for drone shipping
def price_for_drone_shipping(weight):
        if weight <= 2:
            ds_cost = (ds_twolb_price_per_pound * weight)
        elif (weight > 2) and (weight < 7):
            ds_cost = (ds_threelb_to_sixlb_price_per_pound *weight)
        elif (weight > 6) and (weight < 11):
            ds_cost = (ds_sevenlb_to_tenlb_price_per_pound * weight)
        elif weight >=11:
            ds_cost = (ds_elevenlb_or_greater * weight)
        return ds_cost
print(price_for_drone_shipping(48))

def better_cost (weight):
    gs_cost = price_for_ground_shipping(weight)
    ds_cost = price_for_drone_shipping(weight)
    if (gs_cost < ds_cost) and (gs_cost < premium_ground_shipping_rate):
        return "Standard ground - $" +str(gs_cost) + " Premium ground - $" +str(premium_ground_shipping_rate) + ". Drone - $" +str(ds_cost) + ". It is cheaper to use standard ground shipping for your delivery!"
    elif (premium_ground_shipping_rate < gs_cost) and (premium_ground_shipping_rate < ds_cost):
        return "Standard ground - $" +str(gs_cost) + " Premium ground - $" +str(premium_ground_shipping_rate) + ". Drone - $" +str(ds_cost) + ". It is cheaper to use premium ground shipping for your delivery!"
    elif (ds_cost < gs_cost) and (ds_cost < premium_ground_shipping_rate):
        return "Standard ground - $" +str(gs_cost) + " Premium ground - $" +str(premium_ground_shipping_rate) + ". Drone - $" +str(ds_cost) + ". It is cheaper to use drone shipping for your delivery"

print(better_cost(41.5))

