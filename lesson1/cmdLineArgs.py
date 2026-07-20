import argparse

parser =  argparse.ArgumentParser(
    description= "Checking up on you"
)

parser.add_argument(
    "-H", "--health", metavar= "health_status",
    required= True , help= "how you are feeling"

)

args = parser.parse_args()

msg = f"thanks for telling me that you are {args.health}, i have taken note of that"
print(msg)