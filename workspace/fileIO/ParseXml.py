
import xml.dom.minidom
def main():
    doc = xml.dom.minidom.parse("D:\\PYTHON\\workspace\\fileIO\\student.xml")
    #First child is student.
    print (doc.firstChild.tagName)
    print ("***************************")
    # Get all hobbies by tag name hobby
    hobbies = doc.getElementsByTagName("hobby")
    # Print the number of hobbies
    print ("%d hobbies:" % hobbies.length)
    #loop through and list all the hobbies
    for activities in hobbies:
        print (activities.getAttribute("name"))
    #Add a new hobby
    newhobby = doc.createElement("hobby")
    newhobby.setAttribute("name", "Basket Ball")
    doc.firstChild.appendChild(newhobby)
    print ("***************************")
    #print all hobbies
    hobbies = doc.getElementsByTagName("hobby")
    print ("%d hobbies:" % hobbies.length)
    for activities in hobbies:
        print (activities.getAttribute("name"))     #First child is student.
    print (doc.firstChild.tagName)
    print ("***************************")
    # Get all hobbies by tag name hobby
    hobbies = doc.getElementsByTagName("hobby")
    # Print the number of hobbies
    print ("%d hobbies:" % hobbies.length)
    #loop through and list all the hobbies
    for activities in hobbies:
        print (activities.getAttribute("name"))
    #Add a new hobby
    newhobby = doc.createElement("hobby")
    newhobby.setAttribute("name", "Basket Ball")
    doc.firstChild.appendChild(newhobby)
    print ("***************************")
    #print all hobbies
    hobbies = doc.getElementsByTagName("hobby")
    print ("%d hobbies:" % hobbies.length)
    for activities in hobbies:
        print (activities.getAttribute("name")) 

if __name__ == "__main__":
    main();
