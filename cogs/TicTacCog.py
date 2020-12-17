import discord
from discord.ext import commands

class TicTacToe(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.turn = 1
        self.piece = "X"
        self.spaces = [' '] * 9
        self.players = []

    async def display(self, message):
        await message.channel.send("```\n" + self.spaces[0] + "|" + self.spaces[1] + "|" + self.spaces[2] + "\n"
                                   + "-+-+-" + "\n" +
                                   self.spaces[3] + "|" + self.spaces[4] + "|" + self.spaces[5] + "\n"
                                   + "-+-+-" + "\n" +
                                   self.spaces[6] + "|" + self.spaces[7] + "|" + self.spaces[8] + "```")

    async def update(self, message, placement, piece):
        if(not (0 <= placement and placement <= 8)):
            await message.channel.send("Invalid placement! Please enter in a valid placement: ")
            await self.display(message)
            return False
        if(self.spaces[placement] == "X" or self.spaces[placement] == "O"):
            await message.channel.send("Space is already filled! Please select another space:")
            await self.display(message)
            return False
        else:
            self.spaces[placement] = piece
            return True

    @commands.command()
    async def run(self, message):

        self.turn = 1
        self.piece = "X"
        self.spaces = [' '] * 9

        await message.channel.send("Welcome to Tic-Tac-Toe!")

        for _ in range(9):
            await message.channel.send("It is X's turn! Please enter an empty space (0-8): ")
            await self.display(message)
            m = await self.bot.wait_for("message")
            placement = int(m.content)
            if(await self.update(message, placement, self.piece)):
                self.turn = self.turn + 1
                self.piece = "O"
            else:
                m = await self.bot.wait_for("message")
                placement = int(m.content)
                await self.update(message, placement, self.piece)
            
            if(await self.checkWinner(message)):
                return
            
            await message.channel.send("It is O's turn! Please enter an empty space (0-8): ")
            await self.display(message)
            m = await self.bot.wait_for("message")
            placement = int(m.content)
            if(await self.update(message, placement, self.piece)):
                self.turn = self.turn + 1
                self.piece = "X"
            else:
                m = await self.bot.wait_for("message")
                placement = int(m.content)
                self.update(message, placement, self.piece)

            if(await self.checkWinner(message)):
                return

    async def checkWinner(self, message):
        if (self.spaces[0] == self.spaces[1] == self.spaces[2] != " "):
            await message.channel.send(self.spaces[0] + " wins!")
            await self.display(message)
            return 1
        elif (self.spaces[3] == self.spaces[4] == self.spaces[5] != " "):
            await message.channel.send(self.spaces[3] + " wins!")
            await self.display(message)
            return 1
        elif (self.spaces[6] == self.spaces[7] == self.spaces[8] != " "):
            await message.channel.send(self.spaces[6] + " wins!")
            await self.display(message)
            return 1
        elif (self.spaces[0] == self.spaces[3] == self.spaces[6] != " "):
            await message.channel.send(self.spaces[0] + " wins!")
            await self.display(message)
            return 1
        elif (self.spaces[1] == self.spaces[4] == self.spaces[7] != " "):
            await message.channel.send(self.spaces[1] + " wins!")
            await self.display(message)
            return 1
        elif (self.spaces[2] == self.spaces[5] == self.spaces[8] != " "):
            await message.channel.send(self.spaces[2] + " wins!")
            await self.display(message)
            return 1
        elif (self.spaces[0] == self.spaces[4] == self.spaces[8] != " "):
            await message.channel.send(self.spaces[0] + " wins!")
            await self.display(message)
            return 1
        elif (self.spaces[2] == self.spaces[4] == self.spaces[6] != " "):
            await message.channel.send(self.spaces[2] + " wins!")
            await self.display(message)
            return 1

    @commands.command()
    async def challenge(self, ctx, opponent: discord.User):
        if ctx.author == opponent:
            await ctx.send("You cannot challenge yourself!")
        elif opponent.bot:
            await ctx.send("You cannot challenge a Discord bot!")
        else:
            user1 = "<@" + str(ctx.author.id) + ">"
            user2 = "<@" + str(opponent.id) + ">"

            await ctx.send(user1 + " has challenged " + user2 + " to a game of Tic-Tac-Toe!")

            self.players = [ctx.author.id, opponent.id]

def setup(bot):
    bot.add_cog(TicTacToe(bot))