from get_solcast_forecast import get_solcast_forecast
from get_weekly_average import get_weekly_average
from set_battery import set_battery_charge

def configure_battery():
    #get consumption
    daily_totals = get_weekly_average()
    average_consumption = sum(daily_totals)/len(daily_totals)

    #get forecast
    tomorrow_forecast = get_solcast_forecast()
    print(tomorrow_forecast, average_consumption)
    
    if tomorrow_forecast > average_consumption:
        set_battery_charge(0)

    else:
        set_battery_charge(100)   

    return   