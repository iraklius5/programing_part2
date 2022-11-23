public class Main {

    public static void main(String[] args) {
        System.out.println("-----Lab1------");

        Hotel hotel1 = new Hotel();
        Hotel hotel2 = new Hotel("Lviv holel", 200, 8500);
        Hotel hotel3 = new Hotel("Sambir", 20, 2000,
                false, true, 3);

        System.out.println(hotel1.toString());
        System.out.println(hotel2.toString());
        System.out.println(hotel3.toString());

        System.out.println("Country: " + Hotel.getCountry());
    }
}
