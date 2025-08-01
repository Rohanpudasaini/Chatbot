import asyncio
import warnings
from typing import Any, Dict, Optional

from rasa.core.agent import Agent

warnings.filterwarnings("ignore")


# A placeholder for your Whisper function (remains the same)
def get_text_from_voice() -> str:
    """
    This function represents your Whisper model.
    It captures voice and returns the transcribed text.
    """
    # Simulate the output from Whisper
    # user_voice_input = "I want to do a card to card transaction"
    # print(f"🎤 Whisper transcribed text: '{user_voice_input}'")
    user_voice_input = input("Enter your command: ")
    return user_voice_input


# --- RASA NLU PROCESSOR CLASS (Updated for Rasa 3.x) ---


class NLUProcessor:
    """
    A class to load a Rasa model and use it for NLU-only tasks.
    """

    def __init__(self, agent: Agent):
        """
        Private constructor. Use the `create` classmethod to instantiate.
        """
        self.agent = agent
        if self.agent:
            print("✅ Rasa NLUProcessor initialized successfully.")

    @classmethod
    def create(cls, model_path: str) -> Optional["NLUProcessor"]:
        """
        Asynchronously loads the Rasa model and returns a class instance.

        Args:
            model_path: Path to the trained Rasa model (.tar.gz).

        Returns:
            An instance of NLUProcessor, or None if loading fails.
        """
        try:
            # Use Agent.load() to load the model. This is the correct method in Rasa 3.x.
            agent = Agent.load(model_path=model_path)
            return cls(agent)
        except Exception as e:
            print(f"❌ Error loading Rasa model: {e}")
            return None

    async def classify_intent(self, text: str) -> Optional[Dict[str, Any]]:
        """
        Uses the loaded agent to classify the intent of the given text.

        Args:
            text: The user input text.

        Returns:
            The classification result dictionary from Rasa, or None.
        """
        if not self.agent:
            print("Agent not available. Cannot classify intent.")
            return None

        # agent.parse_message() returns a list containing one dictionary.
        result = await self.agent.parse_message(text)
        return result or None

    async def process_command(self, text: str, confidence_threshold: float = 0.80):
        """
        Processes a text command, classifies it, and prints the determined action.

        Args:
            text: The user input text.
            confidence_threshold: The minimum confidence to consider an intent valid.
        """
        classification_result = await self.classify_intent(text)

        if classification_result:
            intent = classification_result.get("intent", {})
            intent_name = intent.get("name")
            confidence = intent.get("confidence")

            print("\n--- Rasa NLU Analysis ---")
            print(f"Intent: {intent_name}")
            print(f"Confidence: {confidence:.2f}")

            # Your application logic based on the intent
            if confidence and confidence > confidence_threshold:
                if intent_name == "send_money":
                    print("\nAction: 🚀 Initiating 'send money' flow...")
                elif intent_name == "top_up":
                    print("\nAction: 📱 Initiating 'mobile top-up' flow...")
                elif intent_name == "card_to_card_transfer":
                    print("\nAction: 💳 Initiating 'card to card transfer' flow...")
                else:
                    print(
                        f"\nAction: 🤔 Intent recognized, but no specific action is defined. {intent_name}"
                    )
            else:
                print(
                    f"\nAction: 🤷 Could not determine action. Confidence ({confidence:.2f}) is below threshold ({confidence_threshold})."
                )


# --- MAIN EXECUTION LOGIC ---


async def main():
    """
    Main function to set up and run the NLU processor.
    """
    # Path to your trained NLU model
    # The filename will be something like 'nlu-YYYYMMDD-HHMMSS.tar.gz'
    # Since the current date is August 1, 2025, let's use a plausible filename.
    NLU_MODEL_PATH = "./models/nlu-20250801-101311-wintry-cod.tar.gz"  # <-- IMPORTANT: Change this path

    # 1. Create an instance of the NLUProcessor
    processor = NLUProcessor.create(NLU_MODEL_PATH)

    if processor:
        # 2. Get text from user's voice command via Whisper
        user_command = get_text_from_voice()

        # 3. Pass the text to the processor to handle it
        if user_command:
            await processor.process_command(user_command)


if __name__ == "__main__":
    asyncio.run(main())
