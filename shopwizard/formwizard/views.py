import base64

from django.views.generic.edit import FormView

from .forms import ShopForm1, ShopForm2, ShopForm3, ShopForm4, ShopForm5


class Step1(FormView):
    template_name = "formwizard/step1.html"
    form_class = ShopForm1
    success_url = "/step2/"

    def get_initial(self):
        form_data = self.request.session.get("step1_data", None)

        if form_data is not None:
            form_data['logo'] = None # Jak na razie resetujemy te pole na wszelki wypadek
            return form_data
        return super().get_initial()

    def form_valid(self, form):
        im = self.request.FILES['logo']

        # Zamieniamy obraz na str, by móc go przechowywać w session
        str_img = base64.b64encode(im.read()).decode('ascii')

        # typ UploadedFile nie da się serializować, więc usuwamy go z dicta
        # by session się nim nie zakrztusił
        data = form.cleaned_data
        data.pop('logo')

        self.request.session["step1_data"] = data
        self.request.session["im1"] = str_img
        # Process the form here
        return super().form_valid(form)


class GenericStep(FormView):
    data_name = "" # The name of the key in the session dict containing previous form data

    def get_initial(self):
        form_data = self.request.session.get(self.data_name, None)

        if form_data is not None:
            return form_data
        return super().get_initial()

    def form_valid(self, form):
        if self.data_name != "":
            self.request.session[self.data_name] = form.cleaned_data
        return super().form_valid(form)


class Step2(GenericStep):
    template_name = "formwizard/step2.html"
    form_class = ShopForm2
    success_url = "/step3/"
    data_name = "step2_data"


class Step3(GenericStep):
    template_name = "formwizard/step3.html"
    form_class = ShopForm3
    success_url = "/step4/"
    data_name = "step3_data"


class Step4(GenericStep):
    template_name = "formwizard/step4.html"
    form_class = ShopForm4
    success_url = "/step5/"
    data_name = "step4_data"


class Step5(GenericStep):
    template_name = "formwizard/step5.html"
    form_class = ShopForm5
    success_url = "/step5/"
    data_name = "step5_data"
    