public class App {


    public static String encode(String string){
        char currentChar = string.charAt(0);
        int charCount = 0;
        String encodedString = "";
        for (int i = 0; i < string.length(); i++) {
            if(currentChar == (string.charAt(i))){
                charCount++;
            }
            else{
                encodedString += String.valueOf(charCount) + currentChar;
                currentChar = string.charAt(i);
                charCount = 1;
            }
        }
        encodedString += String.valueOf(charCount) + currentChar;
        return encodedString;
    }
    public static String decode(String string){
        String decodedString ="";
        for (int i = 0; i < string.length(); i+=2) {
            for (int j = 0; j < Character.getNumericValue(string.charAt(i)); j++) {
                decodedString += string.charAt(i+1); 
            }
            
        }
        return decodedString;
    }

    public static void main(String[] args) throws Exception {
        System.out.println("Hello, World!");

        System.out.println(encode("AAAABBBCCDAA"));

        System.out.println(decode("4A3B2C1D2A"));

    }
}
