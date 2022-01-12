from discord.ext import commands
class g_r_mod(commands.Cog):
	def __init__(self,bot):
		self.bot=bot
	@commands.Cog.listener()
	#on ready function to display login :)
	async def on_ready(self):
		print(f"logged in as :: >> {self.bot.user.name}")

	
	@commands.Cog.listener()
	async def on_member_join(self,member):
		#welcomes new users to server :)
		channel=member.guild.system_channel
		await channel.send(f"Hello {member} . welcome to g-tech test server :)")

	@commands.Cog.listener()
	async def on_reaction_add(self,reaction,user):
		#notify when users react to messages :)
		channel=reaction.message.channel
		async for user in reaction.users():
			await channel.send(f"<{user.name}> gave reaction to user <{reaction.message.author.name}> with {reaction.emoji}")

	@commands.command()
	async def help(self,ctx):
		#send help message
		await ctx.send(f"Hello i am g-tech test bot.the following commands are available.\n1>!help :- provide help menu \n2>!role <role_name> :- creates role of name \"role_name\" and assigns the role\n3>!register <name> :- registers the given name in database\n4>!names :- displays the names registered in database if the user has admin role")

	@commands.Cog.listener()
	async def on_command_error(self,ctx,error): 
		if isinstance(error, commands.CommandNotFound): 
			await ctx.send("Command not found!")
			
def setup(bot):
	bot.add_cog(g_r_mod(bot))	
		