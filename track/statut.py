import nextcord
from nextcord.ext import commands, tasks
import json
from datetime import datetime

class StatusTrackingCogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.user_id = 1148991156571611197
        self.update_stats.start()

    @tasks.loop(seconds=2)
    async def update_stats(self):
        await self.bot.wait_until_ready()
        user = self.bot.get_user(self.user_id)
        
        if user:
            user_status = str(user.status)
            print(user_status)
            timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            
            with open("user_status.json", "r") as file:
                old_status = json.load(file)
            
            if user_status != old_status["status"]:
                status_data = {
                    "user_id": self.user_id,
                    "status": user_status,
                    "timestamp": timestamp
                }
                
                with open("user_status.json", "w") as file:
                    json.dump(status_data, file)

    @update_stats.before_loop
    async def before_update_stats(self):
        await self.bot.wait_until_ready()

def setup(bot):
    bot.add_cog(StatusTrackingCogs(bot))
