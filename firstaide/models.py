from django.db import models

class SeekingStaffSupport(models.Model):
	post_id = models.CharField(max_length=21, default= "seeking-staff-support", editable=False)
	page_type = models.CharField(max_length= 14, default= "full_page_card", editable=False)
	title = models.CharField(max_length=200, null = False)
	content = models.CharField(max_length= 5000, null= False)

	def __str__(self):
		return self.post_id

	class Meta:
		verbose_name = 'Seeking Staff Support'

class SexualAssault(models.Model):
	post_id = models.CharField(max_length=14, default= "sexual-assault", editable=False)
	page_type = models.CharField(max_length= 14, default= "full_page_card", editable=False)
	title = models.CharField(max_length=200, null = False)
	content = models.CharField(max_length= 5000, null= False)

	def __str__(self):
		return self.post_id

	class Meta:
		verbose_name = 'Sexual Assault'

class SexualHarassment(models.Model):
	post_id = models.CharField(max_length=17, default= "sexual-harassment", editable=False)
	page_type = models.CharField(max_length= 14, default= "full_page_card", editable=False)
	title = models.CharField(max_length=200, null = False)
	content = models.CharField(max_length= 5000, null= False)

	def __str__(self):
		return self.post_id

	class Meta:
		verbose_name = 'Sexual Harassment'

class SexualAssaultMore(models.Model):
	post_id = models.CharField(max_length=19, default= "sexual-assault-more", editable=False)
	page_type = models.CharField(max_length= 14, default= "full_page_card", editable=False)
	title = models.CharField(max_length=200, null = False)
	content = models.CharField(max_length= 5000, null= False)

	def __str__(self):
		return self.post_id

	class Meta:
		verbose_name = 'Sexual Assault More'

class Glossary(models.Model):
	post_id = models.CharField(max_length=7, default= "glossary", editable=False)
	page_type = models.CharField(max_length= 14, default= "full_page_card", editable=False)
	title = models.CharField(max_length=200, null = False)
	content = models.CharField(max_length= 5000, null= False)

	def __str__(self):
		return self.post_id

	class Meta:
		verbose_name = 'Glosarry'

class PolicySummary(models.Model):
	post_id = models.CharField(max_length=14, default= "policy-summary", editable=False)
	page_type = models.CharField(max_length= 14, default= "full_page_card", editable=False)
	title = models.CharField(max_length=200, null = False)
	content = models.CharField(max_length= 5000, null= False)

	def __str__(self):
		return self.post_id

	class Meta:
		verbose_name = 'Policy Summary'

class FurtherResources(models.Model):
	post_id = models.CharField(max_length=14, default= "further-resources", editable=False)
	page_type = models.CharField(max_length= 14, default= "full_page_card", editable=False)
	title = models.CharField(max_length=200, null = False)
	content = models.CharField(max_length= 5000, null= False)

	def __str__(self):
		return self.post_id

	class Meta:
		verbose_name = 'Further Resources'

class PeaceCorpsCommitment(models.Model):
	post_id = models.CharField(max_length=21, default= "peace-corps-commitment", editable=False)
	page_type = models.CharField(max_length= 14, default= "full_page_card", editable=False)
	title = models.CharField(max_length=200, null = False)
	content = models.CharField(max_length= 5000, null= False)

	def __str__(self):
		return self.post_id

	class Meta:
		verbose_name = 'Peace Corps Commitment'

class Confidentiality(models.Model):
	post_id = models.CharField(max_length=15, default= "confidentiality", editable=False)
	page_type = models.CharField(max_length= 14, default= "full_page_card", editable=False)
	title = models.CharField(max_length=200, null = False)
	content = models.CharField(max_length= 5000, null= False)

	def __str__(self):
		return self.post_id

	class Meta:
		verbose_name = 'Confidentiality'

class PageAddedSoon(models.Model):
	post_id = models.CharField(max_length=15, default= "page-added-soon", editable=False)
	page_type = models.CharField(max_length= 14, default= "full_page_card", editable=False)
	title = models.CharField(max_length=200, null = False)
	content = models.CharField(max_length= 5000, null= False)

	def __str__(self):
		return self.post_id

	class Meta:
		verbose_name = 'Page Added Soon'


class ServicesAfterAssault(models.Model):
	post_id = models.CharField(max_length=22, default= "services-after-assault", editable=False)
	page_type = models.CharField(max_length= 16, default= "multi_cards_page", editable=False)
	title = models.CharField(max_length=200, null = False)
	content = models.CharField(max_length= 5000, null= False)

	def __str__(self):
		return self.post_id

	class Meta:
		verbose_name = 'Services After Assault'

class Radar(models.Model):
	post_id = models.CharField(max_length=5, default= "radar", editable=False)
	page_type = models.CharField(max_length= 16, default= "multi_cards_page", editable=False)
	title = models.CharField(max_length=200, null = False)
	content = models.CharField(max_length= 5000, null= False)

	def __str__(self):
		return self.post_id

	class Meta:
		verbose_name = 'Radar'

class SexualPredators(models.Model):
	post_id = models.CharField(max_length=16, default= "sexual-predators", editable=False)
	page_type = models.CharField(max_length= 16, default= "multi_cards_page", editable=False)
	title = models.CharField(max_length=200, null = False)
	content = models.CharField(max_length= 5000, null= False)

	def __str__(self):
		return self.post_id

	class Meta:
		verbose_name = 'Sexual Predators'

class ImpactOfAssault(models.Model):
	post_id = models.CharField(max_length=17, default= "impact-of-assault", editable=False)
	page_type = models.CharField(max_length= 16, default= "multi_cards_page", editable=False)
	title = models.CharField(max_length=200, null = False)
	content = models.CharField(max_length= 5000, null= False)

	def __str__(self):
		return self.post_id

	class Meta:
		verbose_name = 'Impact Of Assault'

class HelpAFriend(models.Model):
	post_id = models.CharField(max_length=13, default= "help-a-friend", editable=False)
	page_type = models.CharField(max_length= 16, default= "multi_cards_page", editable=False)
	title = models.CharField(max_length=200, null = False)
	content = models.CharField(max_length= 5000, null= False)

	def __str__(self):
		return self.post_id

	class Meta:
		verbose_name = 'Help a friend'

class SafetyPlanBasics(models.Model):
	post_id = models.CharField(max_length=18, default= "safety-plan-basics", editable=False)
	page_type = models.CharField(max_length= 16, default= "multi_cards_page", editable=False)
	title = models.CharField(max_length=200, null = False)
	content = models.CharField(max_length= 5000, null= False)

	def __str__(self):
		return self.post_id

	class Meta:
		verbose_name = 'Safety Plan Basics'

class UnwantedAttention(models.Model):
	post_id = models.CharField(max_length=18, default= "unwanted-attention", editable=False)
	page_type = models.CharField(max_length= 16, default= "multi_cards_page", editable=False)
	title = models.CharField(max_length=200, null = False)
	content = models.CharField(max_length= 5000, null= False)

	def __str__(self):
		return self.post_id

	class Meta:
		verbose_name = 'Unwanted Attention'

class BystanderIntervention(models.Model):
	post_id = models.CharField(max_length=22, default= "bystander-intervention", editable=False)
	page_type = models.CharField(max_length= 16, default= "multi_cards_page", editable=False)
	title = models.CharField(max_length=200, null = False)
	content = models.CharField(max_length= 5000, null= False)

	def __str__(self):
		return self.post_id

	class Meta:
		verbose_name = 'Bystander Intervention'

class CommonQuestions(models.Model):
	post_id = models.CharField(max_length=16, default= "common-questions", editable=False)
	page_type = models.CharField(max_length= 18, default= "multi_segment_page", editable=False)
	title = models.CharField(max_length=200, null = False)
	content = models.CharField(max_length= 5000, null= False)

	def __str__(self):
		return self.post_id

	class Meta:
		verbose_name = 'Common Questions'

class SafetyPlanWorksheet(models.Model):
	post_id = models.CharField(max_length=21, default= "safety-plan-worksheet", editable=False)
	page_type = models.CharField(max_length= 18, default= "multi_segment_page", editable=False)
	title = models.CharField(max_length=200, null = False)
	content = models.CharField(max_length= 5000, null= False)

	def __str__(self):
		return self.post_id

	class Meta:
		verbose_name = 'Safety Plan Worksheet'

class Mythbusters(models.Model):
	post_id = models.CharField(max_length=11, default= "mythbusters", editable=False)
	page_type = models.CharField(max_length= 27, default= "multi_segment_vertical_page", editable=False)
	title = models.CharField(max_length=200, null = False)
	content = models.CharField(max_length= 5000, null= False)

	def __str__(self):
		return self.post_id

	class Meta:
		verbose_name = 'Mythbusters'
