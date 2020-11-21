class Graph:
    def __init__(self, vertices_lst):
        self.weight = dict()
        for src in vertices_lst:
            self.weight[src] = []

    def add_edge(self, start, end, weight=0, undirect=False):
        if self.weight.get(start, -1) == -1:
            self.weight[start] = []
        if [end, weight] not in self.weight[start]:
            self.weight[start].append([end, weight])
        if undirect:
            if self.weight.get(end, -1) == -1:
                self.weight[end] = []
            if [start, weight] not in self.weight[end]:
                self.weight[end].append([start, weight])

    def _min_distance(self, dist, visited):
        minimum = 9999999999999
        tmp = list(self.weight.keys())
        min_index = tmp[0]
        for vertex in self.weight:
            if dist[vertex][0] < minimum and vertex not in visited:
                minimum = dist[vertex][0]
                min_index = vertex
        return min_index

    def dijkstra(self, start):
        visited = set()
        dist = dict()
        for vertex in self.weight:
            dist[vertex] = [999999999999999999, vertex]
        dist[start] = [0, start]
        for key in self.weight:
            u = self._min_distance(dist, visited)
            visited.add(u)
            for pair in self.weight[u]:  # every vertex that connected to u
                v = pair[0]
                w = pair[1]
                if v not in visited and dist[v][0] > dist[u][0]+w:
                    dist[v][0] = dist[u][0]+w
                    dist[v][1] = u
        return dist

    def dijkstra_AB(self, src, dest):
        dist = self.dijkstra(src)
        if dist[dest][0] == 999999999999999999:
            print(f"Not have path : {src} to {dest}")
            return
        if src == dest:
            return [src]
        lst = [src]
        curr = dest
        stack = []
        while curr != src:
            stack.append(curr)
            curr = dist[curr][1]
        while len(stack) > 0:
            lst.append(stack.pop())

        return lst

    def __str__(self):
        return str(self.weight)


if __name__ == '__main__':
    station = {
        "Acton Town": ["Ealing Common", "South Ealing", "Turnham Green", "Chiswick Park"],
        "Aldgate": ["Liverpool Street", "Tower Hill"],
        "Aldgate East": ["Tower Hill", "Whitechapel", "Liverpool Street"],
        "All Saints": ["Devons Road", "Poplar"],
        "Alperton": ["Park Royal", "Sudbury Town"],
        "Amersham": ["Chalfont & Latimer"],
        "Angel": ["King's Cross St. Pancras", "Old Street"],
        "Archway": ["Highgate", "Tufnell Park"],
        "Arnos Grove": ["Bounds Green", "Southgate"],
        "Arsenal": ["Finsbury Park", "Holloway Road"],
        "Baker Street": ["Marylebone", "Regent's Park", "Edgware Road (C)", "Great Portland Street", "Bond Street", "St. John's Wood", "Finchley Road"],
        "Balham": ["Clapham South", "Tooting Bec"],
        "Bank": ["Liverpool Street", "St. Paul's", "Shadwell", "London Bridge", "Moorgate", "Waterloo"],
        "Barbican": ["Farringdon", "Moorgate"],
        "Barking": ["East Ham", "Upney"],
        "Barkingside": ["Fairlop", "Newbury Park"],
        "Barons Court": ["Hammersmith", "West Kensington", "Earl's Court"],
        "Bayswater": ["Notting Hill Gate", "Paddington"],
        "Beckton": ["Gallions Reach"],
        "Beckton Park": ["Cyprus", "Royal Albert"],
        "Becontree": ["Dagenham Heathway", "Upney"],
        "Belsize Park": ["Chalk Farm", "Hampstead"],
        "Bermondsey": ["Canada Water", "London Bridge"],
        "Bethnal Green": ["Liverpool Street", "Mile End"],
        "Blackfriars": ["Mansion House", "Temple"],
        "Blackhorse Road": ["Tottenham Hale", "Walthamstow Central"],
        "Blackwall": ["East India", "Poplar"],
        "Bond Street": ["Marble Arch", "Oxford Circus", "Green Park", "Baker Street"],
        "Borough": ["Elephant & Castle", "London Bridge"],
        "Boston Manor": ["Northfields", "Osterley"],
        "Bounds Green": ["Wood Green", "Arnos Grove"],
        "Bow Church": ["Devons Road", "Pudding Mill Lane"],
        "Bow Road": ["Bromley-By-Bow", "Mile End"],
        "Brent Cross": ["Golders Green", "Hendon Central"],
        "Brixton": ["Stockwell"],
        "Bromley-By-Bow": ["West Ham", "Bow Road"],
        "Buckhurst Hill": ["Loughton", "Woodford"],
        "Burnt Oak": ["Colindale", "Edgware"],
        "Caledonian Road": ["Holloway Road", "King's Cross St. Pancras"],
        "Camden Town": ["Chalk Farm", "Euston", "Kentish Town", "Mornington Crescent"],
        "Canada Water": ["Rotherhithe", "Surrey Quays", "Canary Wharf", "Bermondsey"],
        "Canary Wharf": ["Heron Quays", "West India Quay", "North Greenwich", "Canada Water"],
        "Canning Town": ["East India", "Royal Victoria", "North Greenwich", "West Ham"],
        "Cannon Street": ["Mansion House", "Monument"],
        "Canons Park": ["Queensbury", "Stanmore"],
        "Chalfont & Latimer": ["Chesham", "Chorleywood", "Amersham"],
        "Chalk Farm": ["Belsize Park", "Camden Town"],
        "Chancery Lane": ["Holborn", "St. Paul's"],
        "Charing Cross": ["Embankment", "Picadilly Circus", "Leicester Square"],
        "Chesham": ["Chalfont & Latimer"],
        "Chigwell": ["Grange Hill", "Roding Valley"],
        "Chiswick Park": ["Acton Town", "Turnham Green"],
        "Chorleywood": ["Rickmansworth", "Chalfont & Latimer"],
        "Clapham Common": ["Clapham North", "Clapham South"],
        "Clapham North": ["Stockwell", "Clapham Common"],
        "Clapham South": ["Balham", "Clapham Common"],
        "Cockfosters": ["Oakwood"],
        "Colindale": ["Hendon Central", "Burnt Oak"],
        "Colliers Wood": ["South Wimbledon", "Tooting Broadway"],
        "Covent Garden": ["Holborn", "Leicester Square"],
        "Crossharbour & London Arena": ["Mudchute", "South Quay"],
        "Croxley": ["Moor Park", "Watford"],
        "Custom House": ["Prince Regent", "Royal Victoria"],
        "Cutty Sark": ["Greenwich", "Island Gardens"],
        "Cyprus": ["Gallions Reach", "Beckton Park"],
        "Dagenham East": ["Dagenham Heathway", "Elm Park"],
        "Dagenham Heathway": ["Becontree", "Dagenham East"],
        "Debden": ["Loughton", "Theydon Bois"],
        "Deptford Bridge": ["Elverson Road", "Greenwich"],
        "Devons Road": ["All Saints", "Bow Church"],
        "Dollis Hill": ["Neasden", "Willesden Green"],
        "Ealing Broadway": ["West Acton", "Ealing Common"],
        "Ealing Common": ["Acton Town", "North Ealing", "Ealing Broadway"],
        "Earl's Court": ["Gloucester Road", "High Street Kensington", "Kensington (Olympia)", "West Brompton", "West Kensington", "Barons Court"],
        "East Acton": ["North Acton", "White City"],
        "East Finchley": ["Finchley Central", "Highgate"],
        "East Ham": ["Upton Park", "Barking"],
        "East India": ["Blackwall", "Canning Town"],
        "East Putney": ["Putney Bridge", "Southfields"],
        "Eastcote": ["Rayners Lane", "Ruislip Manor"],
        "Edgware": ["Burnt Oak"],
        "Edgware Road (B)": ["Marylebone", "Paddington"],
        "Edgware Road (C)": ["Paddington", "Baker Street"],
        "Elephant & Castle": ["Lambeth North", "Kennington", "Borough"],
        "Elm Park": ["Hornchurch", "Dagenham East"],
        "Elverson Road": ["Lewisham", "Deptford Bridge"],
        "Embankment": ["Waterloo", "Temple", "Westminster", "Charing Cross"],
        "Epping": ["Theydon Bois"],
        "Euston": ["King's Cross St. Pancras", "Mornington Crescent", "Warren Street", "Camden Town"],
        "Euston Square": ["Great Portland Street", "King's Cross St. Pancras"],
        "Fairlop": ["Hainault", "Barkingside"],
        "Farringdon": ["King's Cross St. Pancras", "Barbican"],
        "Finchley Central": ["Mill Hill East", "West Finchley", "East Finchley"],
        "Finchley Road": ["Swiss Cottage", "West Hampstead", "Wembley Park", "Baker Street"],
        "Finsbury Park": ["Manor House", "Highbury & Islington", "Seven Sisters", "Arsenal"],
        "Fulham Broadway": ["Parsons Green", "West Brompton"],
        "Gallions Reach": ["Beckton", "Cyprus"],
        "Gants Hill": ["Newbury Park", "Redbridge"],
        "Gloucester Road": ["High Street Kensington", "South Kensington", "Earl's Court"],
        "Golders Green": ["Hampstead", "Brent Cross"],
        "Goldhawk Road": ["Hammersmith", "Shepherd's Bush (H)"],
        "Goodge Street": ["Tottenham Court Road", "Warren Street"],
        "Grange Hill": ["Hainault", "Chigwell"],
        "Great Portland Street": ["Baker Street", "Euston Square"],
        "Green Park": ["Westminster", "Hyde Park Corner", "Picadilly Circus", "Oxford Circus", "Victoria", "Bond Street"],
        "Greenford": ["Northolt", "Perivale"],
        "Greenwich": ["Cutty Sark", "Deptford Bridge"],
        "Gunnersbury": ["Kew Gardens", "Turnham Green"],
        "Hainault": ["Fairlop", "Grange Hill"],
        "Hammersmith": ["Ravenscourt Park", "Turnham Green", "Barons Court", "Goldhawk Road"],
        "Hampstead": ["Belsize Park", "Golders Green"],
        "Hanger Lane": ["North Acton", "Perivale"],
        "Harlesden": ["Stonebridge Park", "Willesden Junction"],
        "Harrow & Wealdston": ["Kenton"],
        "Harrow-on-the-Hill": ["Northwick Park", "North Harrow", "West Harrow"],
        "Hatton Cross": ["Heathrow Terminals 1, 2 & 3", "Heathrow Terminal 4", "Hounslow West"],
        "Heathrow Terminal 4": ["Hatton Cross", "Heathrow Terminals 1, 2 & 3"],
        "Heathrow Terminals 1, 2 & 3": ["Heathrow Terminal 4", "Hatton Cross"],
        "Hendon Central": ["Brent Cross", "Colindale"],
        "Heron Quays": ["South Quay", "Canary Wharf"],
        "High Barnet": ["Totteridge & Whetstone"],
        "High Street Kensington": ["Notting Hill Gate", "Earl's Court", "Gloucester Road"],
        "Highbury & Islington": ["King's Cross St. Pancras", "Finsbury Park"],
        "Highgate": ["Archway", "East Finchley"],
        "Hillingdon": ["Ickenham", "Uxbridge"],
        "Holborn": ["Tottenham Court Road", "Russell Square", "Chancery Lane", "Covent Garden"],
        "Holland Park": ["Notting Hill Gate", "Shepherd's Bush (C)"],
        "Holloway Road": ["Arsenal", "Caledonian Road"],
        "Hornchurch": ["Upminster Bridge", "Elm Park"],
        "Hounslow Central": ["Hounslow East", "Hounslow West"],
        "Hounslow East": ["Osterley", "Hounslow Central"],
        "Hounslow West": ["Hatton Cross", "Hounslow Central"],
        "Hyde Park Corner": ["Knightsbridge", "Green Park"],
        "Ickenham": ["Ruislip", "Hillingdon"],
        "Island Gardens": ["Mudchute", "Cutty Sark"],
        "Kennington": ["Oval", "Waterloo", "Elephant & Castle"],
        "Kensal Green": ["Queen's Park", "Willesden Junction"],
        "Kensington (Olympia)": ["Earl's Court"],
        "Kentish Town": ["Tufnell Park", "Camden Town"],
        "Kenton": ["South Kenton", "Harrow & Wealdston"],
        "Kew Gardens": ["Richmond", "Gunnersbury"],
        "Kilburn": ["West Hampstead", "Willesden Green"],
        "Kilburn Park": ["Maida Vale", "Queen's Park"],
        "King's Cross St. Pancras": ["Russell Square", "Angel", "Caledonian Road", "Euston", "Euston Square", "Farringdon", "Highbury & Islington"],
        "Kingsbury": ["Queensbury", "Wembley Park"],
        "Knightsbridge": ["South Kensington", "Hyde Park Corner"],
        "Ladbroke Grove": ["Latimer Road", "Westbourne Park"],
        "Lambeth North": ["Waterloo", "Elephant & Castle"],
        "Lancaster Gate": ["Marble Arch", "Queensway"],
        "Latimer Road": ["Shepherd's Bush (H)", "Ladbroke Grove"],
        "Leicester Square": ["Tottenham Court Road", "Picadilly Circus", "Charing Cross", "Covent Garden"],
        "Lewisham": ["Elverson Road"],
        "Leyton": ["Leytonstone", "Stratford"],
        "Leytonstone": ["Snaresbrook", "Wanstead", "Leyton"],
        "Limehouse": ["Shadwell", "Westferry"],
        "Liverpool Street": ["Moorgate", "Aldgate", "Aldgate East", "Bank", "Bethnal Green"],
        "London Bridge": ["Southwark", "Bank", "Bermondsey", "Borough"],
        "Loughton": ["Buckhurst Hill", "Debden"],
        "Maida Vale": ["Warwick Avenue", "Kilburn Park"],
        "Manor House": ["Turnpike Lane", "Finsbury Park"],
        "Mansion House": ["Blackfriars", "Cannon Street"],
        "Marble Arch": ["Bond Street", "Lancaster Gate"],
        "Marylebone": ["Baker Street", "Edgware Road (B)"],
        "Mile End": ["Stratford", "Stepney Green", "Bethnal Green", "Bow Road"],
        "Mill Hill East": ["Finchley Central"],
        "Monument": ["Tower Hill", "Cannon Street"],
        "Moor Park": ["Northwood", "Rickmansworth", "Croxley"],
        "Moorgate": ["Old Street", "Bank", "Barbican", "Liverpool Street"],
        "Morden": ["South Wimbledon"],
        "Mornington Crescent": ["Camden Town", "Euston"],
        "Mudchute": ["Crossharbour & London Arena", "Island Gardens"],
        "Neasden": ["Wembley Park", "Dollis Hill"],
        "New Cross": ["Surrey Quays"],
        "New Cross Gate": ["Surrey Quays"],
        "Newbury Park": ["Barkingside", "Gants Hill"],
        "North Acton": ["West Acton", "East Acton", "Hanger Lane"],
        "North Ealing": ["Park Royal", "Ealing Common"],
        "North Greenwich": ["Canary Wharf", "Canning Town"],
        "North Harrow": ["Pinner", "Harrow-on-the-Hill"],
        "North Wembley": ["South Kenton", "Wembley Central"],
        "Northfields": ["South Ealing", "Boston Manor"],
        "Northolt": ["South Ruislip", "Greenford"],
        "Northwick Park": ["Preston Road", "Harrow-on-the-Hill"],
        "Northwood": ["Northwood Hills", "Moor Park"],
        "Northwood Hills": ["Pinner", "Northwood"],
        "Notting Hill Gate": ["Queensway", "Bayswater", "High Street Kensington", "Holland Park"],
        "Oakwood": ["Southgate", "Cockfosters"],
        "Old Street": ["Angel", "Moorgate"],
        "Osterley": ["Boston Manor", "Hounslow East"],
        "Oval": ["Stockwell", "Kennington"],
        "Oxford Circus": ["Picadilly Circus", "Regent's Park", "Tottenham Court Road", "Warren Street", "Bond Street", "Green Park"],
        "Paddington": ["Warwick Avenue", "Royal Oak", "Bayswater", "Edgware Road (B)", "Edgware Road (C)"],
        "Park Royal": ["Alperton", "North Ealing"],
        "Parsons Green": ["Putney Bridge", "Fulham Broadway"],
        "Perivale": ["Greenford", "Hanger Lane"],
        "Picadilly Circus": ["Charing Cross", "Green Park", "Leicester Square", "Oxford Circus"],
        "Pimlico": ["Vauxhall", "Victoria"],
        "Pinner": ["North Harrow", "Northwood Hills"],
        "Plaistow": ["Upton Park", "West Ham"],
        "Poplar": ["Westferry", "West India Quay", "All Saints", "Blackwall"],
        "Preston Road": ["Wembley Park", "Northwick Park"],
        "Prince Regent": ["Royal Albert", "Custom House"],
        "Pudding Mill Lane": ["Stratford", "Bow Church"],
        "Putney Bridge": ["East Putney", "Parsons Green"],
        "Queen's Park": ["Kensal Green", "Kilburn Park"],
        "Queensbury": ["Canons Park", "Kingsbury"],
        "Queensway": ["Lancaster Gate", "Notting Hill Gate"],
        "Ravenscourt Park": ["Stamford Brook", "Hammersmith"],
        "Rayners Lane": ["West Harrow", "South Harrow", "Eastcote"],
        "Redbridge": ["Wanstead", "Gants Hill"],
        "Regent's Park": ["Baker Street", "Oxford Circus"],
        "Richmond": ["Kew Gardens"],
        "Rickmansworth": ["Chorleywood", "Moor Park"],
        "Roding Valley": ["Woodford", "Chigwell"],
        "Rotherhithe": ["Wapping", "Canada Water"],
        "Royal Albert": ["Beckton Park", "Prince Regent"],
        "Royal Oak": ["Westbourne Park", "Paddington"],
        "Royal Victoria": ["Canning Town", "Custom House"],
        "Ruislip": ["Ruislip Manor", "Ickenham"],
        "Ruislip Gardens": ["South Ruislip", "West Ruislip"],
        "Ruislip Manor": ["Eastcote", "Ruislip"],
        "Russell Square": ["Holborn", "King's Cross St. Pancras"],
        "Seven Sisters": ["Tottenham Hale", "Finsbury Park"],
        "Shadwell": ["Tower Gateway", "Wapping", "Whitechapel", "Bank", "Limehouse"],
        "Shepherd's Bush (C)": ["White City", "Holland Park"],
        "Shepherd's Bush (H)": ["Goldhawk Road", "Latimer Road"],
        "Shoreditch": ["Whitechapel"],
        "Sloane Square": ["South Kensington", "Victoria"],
        "Snaresbrook": ["South Woodford", "Leytonstone"],
        "South Ealing": ["Acton Town", "Northfields"],
        "South Harrow": ["Sudbury Hill", "Rayners Lane"],
        "South Kensington": ["Gloucester Road", "Knightsbridge", "Sloane Square"],
        "South Kenton": ["Kenton", "North Wembley"],
        "South Quay": ["Crossharbour & London Arena", "Heron Quays"],
        "South Ruislip": ["Northolt", "Ruislip Gardens"],
        "South Wimbledon": ["Colliers Wood", "Morden"],
        "South Woodford": ["Woodford", "Snaresbrook"],
        "Southfields": ["Wimbledon Park", "East Putney"],
        "Southgate": ["Arnos Grove", "Oakwood"],
        "Southwark": ["Waterloo", "London Bridge"],
        "St. James's Park": ["Victoria", "Westminster"],
        "St. John's Wood": ["Swiss Cottage", "Baker Street"],
        "St. Paul's": ["Bank", "Chancery Lane"],
        "Stamford Brook": ["Turnham Green", "Ravenscourt Park"],
        "Stanmore": ["Canons Park"],
        "Stepney Green": ["Whitechapel", "Mile End"],
        "Stockwell": ["Vauxhall", "Brixton", "Clapham North", "Oval"],
        "Stonebridge Park": ["Wembley Central", "Harlesden"],
        "Stratford": ["West Ham", "Leyton", "Mile End", "Pudding Mill Lane"],
        "Sudbury Hill": ["Sudbury Town", "South Harrow"],
        "Sudbury Town": ["Alperton", "Sudbury Hill"],
        "Surrey Quays": ["Canada Water", "New Cross", "New Cross Gate"],
        "Swiss Cottage": ["Finchley Road", "St. John's Wood"],
        "Temple": ["Blackfriars", "Embankment"],
        "Theydon Bois": ["Debden", "Epping"],
        "Tooting Bec": ["Tooting Broadway", "Balham"],
        "Tooting Broadway": ["Colliers Wood", "Tooting Bec"],
        "Tottenham Court Road": ["Goodge Street", "Holborn", "Leicester Square", "Oxford Circus"],
        "Tottenham Hale": ["Blackhorse Road", "Seven Sisters"],
        "Totteridge & Whetstone": ["Woodside Park", "High Barnet"],
        "Tower Gateway": ["Shadwell"],
        "Tower Hill": ["Aldgate", "Aldgate East", "Monument"],
        "Tufnell Park": ["Archway", "Kentish Town"],
        "Turnham Green": ["Acton Town", "Chiswick Park", "Gunnersbury", "Hammersmith", "Stamford Brook"],
        "Turnpike Lane": ["Wood Green", "Manor House"],
        "Upminster": ["Upminster Bridge"],
        "Upminster Bridge": ["Hornchurch", "Upminster"],
        "Upney": ["Barking", "Becontree"],
        "Upton Park": ["East Ham", "Plaistow"],
        "Uxbridge": ["Hillingdon"],
        "Vauxhall": ["Pimlico", "Stockwell"],
        "Victoria": ["Green Park", "Pimlico", "Sloane Square", "St. James's Park"],
        "Walthamstow Central": ["Blackhorse Road"],
        "Wanstead": ["Leytonstone", "Redbridge"],
        "Wapping": ["Rotherhithe", "Shadwell"],
        "Warren Street": ["Euston", "Goodge Street", "Oxford Circus"],
        "Warwick Avenue": ["Maida Vale", "Paddington"],
        "Waterloo": ["Westminster", "Bank", "Embankment", "Kennington", "Lambeth North", "Southwark"],
        "Watford": ["Croxley"],
        "Wembley Central": ["North Wembley", "Stonebridge Park"],
        "Wembley Park": ["Finchley Road", "Kingsbury", "Neasden", "Preston Road"],
        "West Acton": ["Ealing Broadway", "North Acton"],
        "West Brompton": ["Earl's Court", "Fulham Broadway"],
        "West Finchley": ["Woodside Park", "Finchley Central"],
        "West Ham": ["Bromley-By-Bow", "Canning Town", "Plaistow", "Stratford"],
        "West Hampstead": ["Finchley Road", "Kilburn"],
        "West Harrow": ["Harrow-on-the-Hill", "Rayners Lane"],
        "West India Quay": ["Canary Wharf", "Poplar", "Westferry"],
        "West Kensington": ["Barons Court", "Earl's Court"],
        "West Ruislip": ["Ruislip Gardens"],
        "Westbourne Park": ["Ladbroke Grove", "Royal Oak"],
        "Westferry": ["West India Quay", "Limehouse", "Poplar"],
        "Westminster": ["Embankment", "Green Park", "St. James's Park", "Waterloo"],
        "White City": ["East Acton", "Shepherd's Bush (C)"],
        "Whitechapel": ["Aldgate East", "Shadwell", "Shoreditch", "Stepney Green"],
        "Willesden Green": ["Dollis Hill", "Kilburn"],
        "Willesden Junction": ["Harlesden", "Kensal Green"],
        "Wimbledon": ["Wimbledon Park"],
        "Wimbledon Park": ["Southfields", "Wimbledon"],
        "Wood Green": ["Bounds Green", "Turnpike Lane"],
        "Woodford": ["Buckhurst Hill", "Roding Valley", "South Woodford"],
        "Woodside Park": ["Totteridge & Whetstone", "West Finchley"]
    }
    src, dest = input("Enter : ").split(',')
    print(f"From: {src}\nTo: {dest}")
    print("Searching shortest route... This may take a while...")
    g = Graph([])
    for key, lst in station.items():
        for item in lst:
            g.add_edge(key, item, 1, True)
    # print(g.dijkstra(src))
    print("Suggested Route:")
    print(g.dijkstra_AB(src, dest))
