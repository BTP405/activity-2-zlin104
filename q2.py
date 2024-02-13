import matplotlib.pyplot as plt

def graphSnowfall(t):
    #open file for read
    f = open(t, "r")
    """
    remove the whitespaces of each line's value, then convert and store it
    into the data list if the value is digit
    """
    data = [int(line.strip()) for line in f if line.strip().isdigit()]

    #calculate upper start/end point and intervals
    maximun = max(data)
    upperLimit = maximun + 10 - maximun % 10
    lowerLimit = 0
    numInterval = upperLimit // 10
    interval = 10
    
    #calculate the occurrences of each interval
    occurrence = [0] * numInterval
    for snowfall in data:
        value = snowfall-1 if snowfall-1 >= 0 else 0
        index = min(value // 10, numInterval-1)
        occurrence[index] += 1
        
    #create the label and title, draw and show bar graph
    labels = [f'{start+1 if start > 0 else start}-{start + interval}cms'
              for start in range(lowerLimit, upperLimit, 10)
              if start + interval <= upperLimit]
    
    plt.bar(labels, occurrence)
    plt.xlabel('Snowfall Ranges (cm)')
    plt.ylabel('Number of Occurrences')
    plt.title('Snowfall Bar Graph')
    plt.show()


graphSnowfall('t.txt')
