def getItinerary(flights, itinerary):
    # if we used all flights, we're done
    if not flights:
        return itinerary
    
    lastDestination = itinerary[-1]

    for i, (origin, destination) in enumerate(flights):
        if origin == lastDestination:
            # Make a copy of flights without the current one to mark it as used
            flightsWithoutCurrent = flights[:i] + flights[i+1:]
            itinerary.append(destination)
            return getItinerary(flightsWithoutCurrent, itinerary)
    
    return None


if __name__ == '__main__':
    assert getItinerary([('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')], ['YUL']) == ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']
    assert getItinerary([('SFO', 'COM'), ('COM', 'YYZ')] , ['COM']) == None
    assert getItinerary([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], ['A']) == ['A', 'B', 'C', 'A', 'C']
