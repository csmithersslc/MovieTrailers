import media
import fresh_tomatoes

the_illusionist = media.Movie("The Illusionist", 
	"Illusionist reveals mysteries in turn-of-the-century Vienna", 
	"https://upload.wikimedia.org/wikipedia/en/6/6a/The_Illusionist_Poster.jpg", 
	"https://www.youtube.com/watch?v=SpIK6eqop18")


kill_bill_vol1 = media.Movie("Kill Bill Volume 1",
	"The Bride, a former assassin, is betrayed and left for dead by her former leader and lover",
	"https://upload.wikimedia.org/wikipedia/en/c/cf/Kill_bill_vol_one_ver.jpg",
	"https://www.youtube.com/watch?v=ot6C1ZKyiME")

nosferatu = media.Movie("Nosferatu",
	"A young Englishman is sent on a trip to Transylavnia to handle the estates of a feared and myserious Count",
	"https://upload.wikimedia.org/wikipedia/en/9/92/Nosferatuposter.jpg",
	"https://www.youtube.com/watch?v=sMl6hUZHBqY")


contact = media.Movie("Contact",
	"An astronomer makes the greatest discovery of mankind - life outside Earth",
	"https://upload.wikimedia.org/wikipedia/en/7/75/Contact_ver2.jpg",
	"https://www.youtube.com/watch?v=d9C2cF3KvP8")


pans_labyrinth = media.Movie("Pan's Labyrinth",
	"A girl in war-torn WWII Spain finds a new world",
	"https://upload.wikimedia.org/wikipedia/en/6/67/Pan's_Labyrinth.jpg",
	"https://www.youtube.com/watch?v=EXe5a9pBNzg")

shaun_of_the_dead = media.Movie("Shaun of the Dead",
	"A slacker one day finds out his world has been taken over zombies, so he must save his friends, girlfriend, and family",
	"https://upload.wikimedia.org/wikipedia/en/e/ec/Shaun-of-the-dead.jpg",
	"https://www.youtube.com/watch?v=LIfcaZ4pC-4")

army_of_darkness = media.Movie("Army of Darkness",
	"Ash finds out his attempt to escape the Evil Dead has transported him to medieval times",
	"http://vignette2.wikia.nocookie.net/evildead/images/4/46/Army_of_Darkness_poster.jpg/revision/latest?cb=20150719141448",
	"https://www.youtube.com/watch?v=CZ-wU5RXw2o")

the_birds = media.Movie("The Birds",
	"One day, all birds suddenly attack humanity",
	"https://upload.wikimedia.org/wikipedia/commons/c/c0/The_Birds_original_poster.jpg",
	"https://www.youtube.com/watch?v=0fJh2gIBOto")

the_witches = media.Movie("The Witches",
	"Luke discovers witches are real and runs into their leader",
	"https://upload.wikimedia.org/wikipedia/en/3/30/Witches_poster.jpg",
	"https://www.youtube.com/watch?v=d_ZyqaN_XNM")

movies = [the_illusionist, kill_bill_vol1, nosferatu, contact, pans_labyrinth, 
shaun_of_the_dead, army_of_darkness, the_birds, the_witches]

fresh_tomatoes.open_movies_page(movies)

print(media.Movie.__doc__)