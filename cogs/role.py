from discord.ext import commands
import discord

class role(commands.Cog):
	def __init__(self,bot):
		self.bot=bot

	@commands.command()
	async def role(self,ctx,role_name):
		#check if the role_name is not part of moderation roles	
		if role_name not in ["admin","mod","moderator","administrator"]:
			guild=ctx.guild
			#check if the role already exists
			if discord.utils.get(ctx.guild.roles,name=role_name):
				await ctx.send(f"Role <{role_name}> already exists :)")
			else :
				#create role
				await guild.create_role(name=role_name)	
			
			author=ctx.message.author
			#get role from role name 
			role=discord.utils.get(ctx.guild.roles,name=role_name)	
			try :
				#add role to user :)
				await author.add_roles(role)
				#notify user on role assignment
				await ctx.send(f"assigned role <{role_name}> to {author.name}")
			except Exception as err:
				print(err)
		else:
			#notify user that creation of role was not possible as it belongs to moderation roles
			await ctx.send(f"Unable to create role <{role_name}>")		
def setup(bot):
	bot.add_cog(role(bot))	