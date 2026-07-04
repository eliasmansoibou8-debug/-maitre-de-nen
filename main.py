import discord
from discord.ext import commands
from discord import app_commands
import random
import asyncio
import os
import json
intents = discord.Intents.default()

bot = commands.Bot(command_prefix="!", intents=intents)

types_nen = {
    "💪 Renforcement": "Vous excellez dans le renforcement de votre corps et de votre puissance physique.",
    "⚡ Émission": "Vous pouvez projeter votre aura loin de votre corps sans perdre toute son efficacité.",
    "💎 Transmutation": "Votre aura peut imiter les propriétés d'autres matières.",
    "🎭 Matérialisation": "Vous pouvez matérialiser des objets grâce à votre aura.",
    "🎮 Manipulation": "Vous pouvez contrôler des êtres vivants ou des objets grâce à votre aura.",
    "👁️ Spécialisation": "Votre Nen est unique et ne suit aucune règle des autres catégories."
}
def charger_donnees():
    try:
        with open("data.json", "r") as f:
            return json.load(f)
    except:
        return {}

def sauvegarder_donnees(data):
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)
@bot.event
async def on_ready():
    print(f"{bot.user} est connecté.")
    try:
        await bot.tree.sync()
        print("Commandes synchronisées.")
    except Exception as e:
        print(e)

@bot.tree.command(name="eveil", description="Éveille votre Nen")
async def eveil(interaction: discord.Interaction):
    data = charger_donnees()
    user_id = str(interaction.user.id)

    if user_id in data:
        await interaction.response.send_message(
            "❌ Vous avez déjà éveillé votre Nen. Cette commande ne peut être utilisée qu'une seule fois.",
            ephemeral=True
        )
        return
    await interaction.response.send_message(
        "```"
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "        ÉVEIL DU NEN\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Ouverture des nœuds d'aura...\n\n"
        "█░░░░░░░░░ 10%"
        "```"
    )

    await asyncio.sleep(2)

    await interaction.edit_original_response(content=
        "```"
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "        ÉVEIL DU NEN\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Votre aura circule dans tout votre corps...\n\n"
        "█████░░░░░ 50%"
        "```"
    )

    await asyncio.sleep(2)

    await interaction.edit_original_response(content=
        "```"
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "        ÉVEIL DU NEN\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Analyse de l'aura...\n\n"
        "██████████ 100%"
        "```"
    )

    await asyncio.sleep(2)

    nen = random.choice(list(types_nen.keys()))
    data[user_id] = {
        "nen": nen
    }

    sauvegarder_donnees(data)
    embed = discord.Embed(
        title="✨ VOTRE NEN A ÉTÉ ÉVEILLÉ ✨",
        description=f"## {nen}\n\n{types_nen[nen]}",
        color=0x6b46c1
    )

    embed.set_footer(text="Le véritable entraînement commence maintenant...")

    await interaction.edit_original_response(content="", embed=embed)
@bot.tree.command(name="reseteveil", description="Réinitialise l'éveil d'un joueur")
async def reseteveil(interaction: discord.Interaction, membre: discord.Member):

    # Seul ton compte peut utiliser cette commande
    if interaction.user.id != 550742070399205385:
        await interaction.response.send_message(
            "❌ Vous n'êtes pas autorisé à utiliser cette commande.",
            ephemeral=True
        )
        return

    data = charger_donnees()

    user_id = str(membre.id)

    if user_id not in data:
        await interaction.response.send_message(
            "❌ Ce joueur n'a pas encore éveillé son Nen.",
            ephemeral=True
        )
        return

    del data[user_id]
    sauvegarder_donnees(data)

    await interaction.response.send_message(
        f"✅ L'éveil de {membre.mention} a été réinitialisé."
    )
TOKEN = os.getenv("TOKEN")

bot.run(TOKEN)
