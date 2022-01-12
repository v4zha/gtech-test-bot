from discord.ext import commands
import discord
import db_config
class admin(commands.Cog):
	def __init__(self,bot):
		self.bot=bot
	
	@commands.command()
	async def register(self,ctx,name):
		#lazy input sanitization :)
		name=name.strip("-'\"@!._")
		if	name.isalpha():
			if not db_config.user_exist(name):	
				#insert name into db		
				db_config.add_user(name)
			else:
				#notify user that name already exists in db
				await ctx.send(f"name <{name}> already exists")
		else:
			#notify user to enter valid name string :)
			await ctx.send("please enter a valid name :)")

	@commands.command()
	async def names(self,ctx):
		guild=ctx.guild
		author=ctx.message.author
		#get admin role
		role=discord.utils.get(ctx.guild.roles,name="admin")
		#check if user has admin role :)		
		if role in author.roles:
			await ctx.send("names of users in server")
			await ctx.send("========================")
			results=db_config.get_users()
			#get results
			for res in results:
				#iterate through results list and print first element in res touple :) as string
				await ctx.send(res.u_name)
		else:
			#notify user that admin role is required to use this command
			await ctx.send("you should have admin role inorder to view the names")
def setup(bot):
	bot.add_cog(admin(bot))