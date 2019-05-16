from django.forms import BaseForm
from django.core.mail import send_mail


def get_form_defaults(Form: BaseForm):
    form = Form()
    defaults = {}
    for name, field in form.fields.items():
        if field.initial:
            defaults[name] = field.initial
    return defaults


class ListingWithOfferCount(object):
    def __init__(self, listing, num):
        self.listing = listing
        self.num = num


class EmailUtil(object):
    def send_offer_email(offer):
        listing = offer.listing
        apartment = listing.apartment
        buyer = offer.buyer.userinfo
        seller = listing.seller.userinfo
        send_mail(
            f"Castle Apartments: New offer for {apartment}",
            "Hi there from Castle Apartments!, \n\n" +
            "We must inform you that an offer has been made for " +
            f"{apartment} by {seller} for a sum of {offer.request_amount} ISK " +
            f"and the date of conveyance: {offer.request_date}.\n\n" +
            "Have a great day!\n\n For more info, " +
            "feel free to contact us. Phone: +354 123 4567, email: " +
            "castleapartments.vln2@gmail.com",
            "castleapartments.vln2@gmail.com",
            [seller.email, buyer.email],
            fail_silently=True
        )

    def send_sale_complete_email(offer):
        listing = offer.listing
        send_mail(
            "Your sale is complete!",
            "",
            "castleapartments.vln2@gmail.com",
            [offer.buyer.userinfo.email, offer.listing.seller.userinfo.email],
            html_message="" +
            "<p>We are incredibly happy to inform you that you are now the " +
            "proud owner of '{}'.".format(listing.apartment.address) + "</p>" +
            "<p>Please review the information shown below. " +
            "Contact the staff at Castle Apartments for the next steps.</p>" +
            "<h2>Seller</h2>" +
            "<p style='padding-left: 1rem;'>" +
            "<strong>Name:</strong> {}".format(offer.listing.seller.userinfo) +
            "<br />" +
            "<strong>Email:</strong> {}"
            .format(offer.listing.seller.userinfo.email) +
            "<br />" +
            "<strong>Phone:</strong> {}"
            .format(offer.listing.seller.userinfo.phone_number) +
            "</p>" +
            "<h2>Buyer</h2>" +
            "<p style='padding-left: 1rem;'>" +
            "<strong>Name:</strong> {}".format(offer.buyer.userinfo) +
            "<br />" +
            "<strong>Email:</strong> {}"
            .format(offer.buyer.userinfo.email) +
            "<br />" +
            "<strong>Phone:</strong> {}"
            .format(offer.buyer.userinfo.phone_number) +
            "</p>" +
            "<h2>Offer</h2>" +
            "<p style='padding-left: 1rem;'>" +
            "<strong>Property:</strong> {}".format(listing.apartment.address) +
            "<br />" +
            "<strong>Offer amount:</strong> ISK {}"
            .format(offer.request_amount) +
            "<br />" +
            "<strong>Conveyance date:</strong> {}-{}-{}"
            .format(
                offer.request_date.year,
                offer.request_date.month,
                offer.request_date.day
            ) +
            "</p>" +
            "<h2>Contact Us</h2>" +
            "<p style='padding-left: 1rem;'>" +
            "<strong>Email:</strong> castleapartments.vln2@gmail.com" +
            "<br />" +
            "<strong>Phone:</strong> +354 123 4567"
            "</p>",
            fail_silently=True
        )

    def send_sale_decline_email(offer):
        listing = offer.listing
        send_mail(
            "Your sale was cancelled",
            "",
            "castleapartments.vln2@gmail.com",
            [offer.buyer.userinfo.email, offer.listing.seller.userinfo.email],
            html_message="" +
            "<p>We are sad to inform you that you're sale for " +
            "'{}' ".format(listing.apartment.address) +
            "has been cancelled</p>" +
            "<h2>Seller</h2>" +
            "<p style='padding-left: 1rem;'>" +
            "<strong>Name:</strong> {}".format(offer.listing.seller.userinfo) +
            "<br />" +
            "<strong>Email:</strong> {}"
            .format(offer.listing.seller.userinfo.email) +
            "<br />" +
            "<strong>Phone:</strong> {}"
            .format(offer.listing.seller.userinfo.phone_number) +
            "</p>" +
            "<h2>Buyer</h2>" +
            "<p style='padding-left: 1rem;'>" +
            "<strong>Name:</strong> {}".format(offer.buyer.userinfo) +
            "<br />" +
            "<strong>Email:</strong> {}"
            .format(offer.buyer.userinfo.email) +
            "<br />" +
            "<strong>Phone:</strong> {}"
            .format(offer.buyer.userinfo.phone_number) +
            "</p>" +
            "<h2>Offer</h2>" +
            "<p style='padding-left: 1rem;'>" +
            "<strong>Property:</strong> {}".format(listing.apartment.address) +
            "<br />" +
            "<strong>Offer amount:</strong> ISK {}"
            .format(offer.request_amount) +
            "<br />" +
            "<strong>Conveyance date:</strong> {}-{}-{}"
            .format(
                offer.request_date.year,
                offer.request_date.month,
                offer.request_date.day
            ) +
            "</p>" +
            "<h2>Contact Us</h2>" +
            "<p style='padding-left: 1rem;'>" +
            "<strong>Email:</strong> castleapartments.vln2@gmail.com" +
            "<br />" +
            "<strong>Phone:</strong> +354 123 4567"
            "</p>",
            fail_silently=True
        )
