public record Hotel(String name, int roomsCount, int yearsVisitorsCount,
                    boolean isBreakfast, boolean isParking, int starsCount ) {
    static String country = "Ukraine";

    public static String getCountry() {
        return country;
    }

    public Hotel(String name, int roomsCount, int yearsVisitorsCount)  {
        this(name, roomsCount, yearsVisitorsCount, true, true, 4);
    }

    public Hotel() {
        this("Mirabel", 107, 10000, true, true, 4);
    }

    @Override
    public String toString() {
        return  "Hotel name: " + name + "\n" +
                "Stars count: " + starsCount + "\n" +
                "Visitors count per year: " + yearsVisitorsCount + "\n" +
                "Is breakfast: " + isBreakfast + "\n" +
                "Is Parking: " + isParking + "\n" +
                "-------------------------------\n";
    }

}
