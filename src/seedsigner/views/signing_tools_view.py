# Internal file class dependencies
from . import View
from seedsigner.helpers import Buttons, B

# External Dependencies
import time


class SigningToolsView(View):

    def __init__(self, seed_storage) -> None:
        View.__init__(self)
        self.seed_storage = seed_storage

    ###
    ### XPub
    ###

    def display_xpub_info(self, fingerprint, derivation, xpub):
        derivation_display = "Derivation: " + derivation
        xpub_display = xpub[0:7] + "..." + xpub[-9:]
            self.draw_modal(["Empreinte Maître: ", fingerprint, derivation_display, xpub_display], "Info Xpub", "Droite pour Continuer")

    ###
    ### Signing Tx
    ###

<<<<<<< Updated upstream
    def display_transaction_information(self, p) -> None:
        self.draw.rectangle((0, 0, View.canvas_width, View.canvas_height), outline=0, fill=0)

        tw, th = self.draw.textsize("Confirm Tx Details", font=View.ASSISTANT25)
        self.draw.text(((240 - tw) / 2, 3), "Confirm Tx Details", fill=View.color, font=View.ASSISTANT25)
=======
    def display_signed_psbt_animated_qr(self, wallet, psbt) -> None:
        self.draw_modal(["Génération d'un PSBT QR ..."])

        print(psbt)
        images = wallet.make_signing_qr_codes(psbt, SigningToolsView.qr_gen_status)

        cnt = 0
        step = False
        while True:
            if step == False:
                View.DispShowImage(images[cnt])
            else:
                frame_text = (str(cnt+1) + " of " + str(len(images)))
                View.DispShowImageWithText(images[cnt], frame_text)
                time.sleep(0.3)
            if step == False:
                cnt += 1
                if cnt >= len(images):
                    cnt = 0
                wallet.qr_sleep()
                if self.buttons.check_for_low(B.KEY_RIGHT):
                    return
                if self.buttons.check_for_low(B.KEY1):
                    step = True
            else:
                input = self.buttons.wait_for([B.KEY1, B.KEY_RIGHT, B.KEY_UP, B.KEY_DOWN])
                if input == B.KEY_RIGHT:
                    return
                elif input == B.KEY1 or input == B.KEY_DOWN:
                    cnt += 1
                    if cnt >= len(images):
                        cnt = 0
                elif input == B.KEY_UP:
                    cnt -= 1
                    if cnt < 0:
                        cnt = len(images) - 1


    def display_transaction_information(self, wallet) -> None:
        self.draw.rectangle((0, 0, View.canvas_width, View.canvas_height), outline=0, fill=0)

        tw, th = self.draw.textsize("Confirmer les détails de tx", font=View.IMPACT25)
        self.draw.text(((240 - tw) / 2, 3), "Confirmer les détails de tx", fill=View.color, font=View.IMPACT25)
>>>>>>> Stashed changes

        in_fee_outs_str = str(len(p.psbt.inputs))
        in_fee_outs_str += " inputs - fee = " if len(p.psbt.inputs) > 1 else " input - fee = "
        in_fee_outs_str += str(len(p.psbt.outputs))
        in_fee_outs_str += " outs" if len(p.psbt.outputs) > 1 else " out"
        tw, th = self.draw.textsize(in_fee_outs_str, font=View.ASSISTANT22)
        self.draw.text(((240 - tw) / 2, 40), in_fee_outs_str, fill=View.color, font=View.ASSISTANT22)

        receiving_addr_str1 = ""
        receiving_addr_str2 = ""
        if len(p.destination_addresses) > 1:
            receiving_addr_str1 += "multiple"
<<<<<<< Updated upstream
            receiving_addr_str2 += "receiving addresses"
        elif len(p.destination_addresses) == 1:
            receiving_addr_str1 += "receiving address"
            receiving_addr_str2 += "last 13: ... " + p.destination_addresses[0][-13:]
        else:
            receiving_addr_str1 += "Self-Transfer"
        
        tw, th = self.draw.textsize(receiving_addr_str1, font=View.ASSISTANT22)
        self.draw.text(((240 - tw) / 2, 75), receiving_addr_str1, fill=View.color, font=View.ASSISTANT22)
=======
            receiving_addr_str2 += "adresses de réception"
        elif wallet.dest_addr_cnt == 1:
            receiving_addr_str1 += "adresses de réception"
            receiving_addr_str2 += "last 13: ..." + wallet.destinationaddress[-13:]
        else:
            receiving_addr_str1 += "Transfer à soi-même"

        tw, th = self.draw.textsize(receiving_addr_str1, font=View.IMPACT22)
        self.draw.text(((240 - tw) / 2, 75), receiving_addr_str1, fill=View.color, font=View.IMPACT22)
>>>>>>> Stashed changes
        if len(receiving_addr_str2) > 0:
            tw, th = self.draw.textsize(receiving_addr_str2, font=View.ROBOTOCONDENSED_BOLD_18)
            self.draw.text(((240 - tw) / 2, 105), receiving_addr_str2, fill=View.color, font=View.ROBOTOCONDENSED_BOLD_18)


<<<<<<< Updated upstream
        if p.spend_amount > 0:
            spending_str = "Spend: " + str(p.spend_amount) + " sats"
            tw, th = self.draw.textsize(spending_str, font=View.ASSISTANT22)
            self.draw.text(((240 - tw) / 2, 130), spending_str, fill=View.color, font=View.ASSISTANT22)

        if p.change_amount > 0 and len(p.destination_addresses) == 0:
            change_str = "Amount: " + str(p.change_amount) + " sats"
            tw, th = self.draw.textsize(change_str, font=View.ASSISTANT22)
            self.draw.text(((240 - tw) / 2, 155), change_str, fill=View.color, font=View.ASSISTANT22)
        elif p.change_amount > 0:
            change_str = "Change: " + str(p.change_amount) + " sats"
            tw, th = self.draw.textsize(change_str, font=View.ASSISTANT22)
            self.draw.text(((240 - tw) / 2, 155), change_str, fill=View.color, font=View.ASSISTANT22)

        fee_str = "Fee: " + str(p.fee_amount) + " sats"
        tw, th = self.draw.textsize(fee_str, font=View.ASSISTANT22)
        self.draw.text(((240 - tw) / 2, 180), fee_str, fill=View.color, font=View.ASSISTANT22)

        tw, th = self.draw.textsize("Left to Exit, Right to Continue", font=View.ASSISTANT18)
        self.draw.text(((240 - tw) / 2, 215), "Left to Exit, Right to Continue", fill=View.color, font=View.ASSISTANT18)
=======
        if wallet.spend > 0:
            spending_str = "Dépense: " + str(wallet.spend) + " sats"
            tw, th = self.draw.textsize(spending_str, font=View.IMPACT22)
            self.draw.text(((240 - tw) / 2, 130), spending_str, fill=View.color, font=View.IMPACT22)

        if wallet.change > 0 and wallet.dest_addr_cnt == 0:
            change_str = "Quantitée: " + str(int(wallet.change)) + " sats"
            tw, th = self.draw.textsize(change_str, font=View.IMPACT22)
            self.draw.text(((240 - tw) / 2, 155), change_str, fill=View.color, font=View.IMPACT22)
        elif wallet.change > 0:
            change_str = "Change: " + str(int(wallet.change)) + " sats"
            tw, th = self.draw.textsize(change_str, font=View.IMPACT22)
            self.draw.text(((240 - tw) / 2, 155), change_str, fill=View.color, font=View.IMPACT22)

        fee_str = "Frais: " + str(int(wallet.fee)) + " sats"
        tw, th = self.draw.textsize(fee_str, font=View.IMPACT22)
        self.draw.text(((240 - tw) / 2, 180), fee_str, fill=View.color, font=View.IMPACT22)

        tw, th = self.draw.textsize("Gauche pour sortir, Droite pour Continuer", font=View.IMPACT18)
        self.draw.text(((240 - tw) / 2, 215), "Gauche pour sortir, Droite pour Continuer", fill=View.color, font=View.IMPACT18)
>>>>>>> Stashed changes

        View.DispShowImage()

    def qr_gen_status(percentage):
        View.draw.rectangle((0, 0, View.canvas_width, View.canvas_height), outline=0, fill=0)
<<<<<<< Updated upstream
        tw, th = View.draw.textsize("QR Generation", font=View.ASSISTANT25)
        View.draw.text(((240 - tw) / 2, 90), "QR Generation", fill=View.color, font=View.ASSISTANT25)
        tw, th = View.draw.textsize(str(round(percentage)) + "% Complete", font=View.ASSISTANT25)
        View.draw.text(((240 - tw) / 2, 125), str(round(percentage)) + "% Complete", fill=View.color, font=View.ASSISTANT25)
=======
        tw, th = View.draw.textsize("Generation du QR ", font=View.IMPACT25)
        View.draw.text(((240 - tw) / 2, 90), "Generation du QR", fill=View.color, font=View.IMPACT25)
        tw, th = View.draw.textsize(str(round(percentage)) + "% Complète", font=View.IMPACT25)
        View.draw.text(((240 - tw) / 2, 125), str(round(percentage)) + "% Complète", fill=View.color, font=View.IMPACT25)
>>>>>>> Stashed changes
        View.DispShowImage()
