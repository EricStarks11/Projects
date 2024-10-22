using System;

class HumanPlayer
{
    private int points; // the points that the human player has

    public HumanPlayer(int initial)
    {
        points = initial;
    }

    public int GetPoints()
    {
        return points;
    }

    public void WinRound()
    {
        points += 5;
    }

    public void LoseRound()
    {
        points -= 5;
    }

    public string HumanDecision()
    {
        Console.WriteLine("Select your shape (Rock, Paper, Scissors): ");
        string decision = Console.ReadLine();
        return decision;
    }
}

class ComputerPlayer
{
    public string ComputerDecision()
    {
        Random random = new Random();
        int decision = random.Next(1, 4);
        switch (decision)
        {
            case 1:
                return "Rock";
            case 2:
                return "Paper";
            case 3:
                return "Scissors";
            default:
                return "Rock";
        }
    }
}

class RockPaperScissors
{
    public static void Main(string[] args)
    {
        HumanPlayer humanPlayer = new HumanPlayer(5); // Initial points for human player
        ComputerPlayer computerPlayer = new ComputerPlayer();
        while (true)
        {
            Console.WriteLine($"Human Player Points: {humanPlayer.GetPoints()}");
            string humanDecision = humanPlayer.HumanDecision();
            string computerDecision = computerPlayer.ComputerDecision();
            Console.WriteLine($"Computer's decision: {computerDecision}");
            if (humanDecision == computerDecision)
            {
                Console.WriteLine("It's a tie!");
            }
            else if ((humanDecision == "Rock" && computerDecision == "Scissors") ||
                     (humanDecision == "Paper" && computerDecision == "Rock") ||
                     (humanDecision == "Scissors" && computerDecision == "Paper"))
            {
                Console.WriteLine("Human Player wins!");
                humanPlayer.WinRound();
            }
            else
            {
                Console.WriteLine("Computer wins!");
                humanPlayer.LoseRound();
            }

            if (humanPlayer.GetPoints() <= 0)
            {
                Console.WriteLine("Game over. Human player has no points left.");
                break;
            }

            Console.WriteLine("Do you want to play another round? (yes/no)");
            string playAgain = Console.ReadLine();
            if (playAgain.ToLower() != "yes")
                break;
        }
    }
}

