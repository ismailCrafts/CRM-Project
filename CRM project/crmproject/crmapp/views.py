from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from crmapp.models import Customers
from django.db.models import Q


# Home view - shows all customers and handles login POST requests
def home(request):
    customers = Customers.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are an authenticated user, feel free to explore.')
            return redirect('home')
        else:
            messages.success(request, 'Something is off. Please try again...')
            return redirect('home')
    else:
        return render(request, 'home.html', {'customers': customers})

# Log out the currently logged-in user
def logout_user(request):
    logout(request)
    messages.success(request, 'Successfully logged out. Please log in to explore this site.')
    return redirect('home')

# User registration view with validation checks
def register(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # Password confirmation check
        if password1 != password2:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')

        # Username uniqueness check
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('register')

        # Email uniqueness check
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('register')

        # Create new user and save full name
        user = User.objects.create_user(email=email, password=password1, username=username)
        user.first_name = fullname
        user.save()
        messages.success(request, "Registration successful. Please log in.")
    return render(request, 'register.html')

# Display detailed customer record; accessible only to logged-in users
def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Customers.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.error(request, 'You must be logged in to visit this page.')
        return redirect('home')

# Delete a customer record if user is authenticated
def customer_delete(request, pk):
    if request.user.is_authenticated:
        customer_delete = Customers.objects.get(id=pk)
        customer_delete.delete()
        messages.success(request, 'Successfully deleted.')
        return redirect('home')
    else:
        messages.error(request, 'You must be logged in before deleting this record.')
        return redirect('home')

# Add a new customer record with email uniqueness validation
def add_record(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            phone = request.POST['phone']
            address = request.POST['address']
            city = request.POST['city']
            customer_info = request.POST['customer_info']
            image = request.FILES.get('image')

            # Prevent duplicate customer emails
            if Customers.objects.filter(email=email).exists():
                messages.error(request, "Email already exists for another customer.")
                return redirect('add_record')

            # Create and save new customer record
            new_record = Customers(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone,
                address=address,
                city=city,
                customer_info=customer_info,
                image=image
            )
            new_record.save()
            messages.success(request, 'Successfully added a new customer record.')
            return redirect('home')

        # Render form for GET request
        return render(request, 'add_record.html')

    else:
        messages.error(request, 'Please login to perform this action.')
        return redirect('login')

# Update an existing customer record with email and phone uniqueness checks
def update_customer(request, pk):
    if request.user.is_authenticated:
        customer = get_object_or_404(Customers, id=pk)

        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            phone = request.POST['phone']
            address = request.POST['address']
            city = request.POST['city']
            customer_info = request.POST['customer_info']
            image = request.FILES.get('image')

            # Validate email uniqueness excluding current record
            if Customers.objects.filter(email=email).exclude(id=pk).exists():
                messages.error(request, "Email already used by another customer.")
                return redirect('update', pk=pk)

            # Validate phone uniqueness excluding current record
            if Customers.objects.filter(phone=phone).exclude(id=pk).exists():
                messages.error(request, "Mobile number already used by another customer.")
                return redirect('update', pk=pk)

            # Update customer fields
            customer.first_name = first_name
            customer.last_name = last_name
            customer.email = email
            customer.phone = phone
            customer.address = address
            customer.city = city
            customer.customer_info = customer_info
            if image:
                customer.image = image

            customer.save()
            messages.success(request, "Customer updated successfully.")
            return redirect('home')

        # Render update form with current customer data on GET
        context = {'customer': customer}
        return render(request, 'update.html', context)

    else:
        messages.error(request, 'Must be logged in to update customer.')
        return redirect('home')

# Search customers by first name, last name, or email
def search_results(request):
    # Check if user is logged in; if not, redirect with an error message
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in to search.")
        return redirect('home')  # Or 'login' if you have a login page

    # Get the search query from GET parameters
    query = request.GET.get('q')
    results = []

    if query:
        # Split the query to check if it's a full name (first and last)
        name_parts = query.split()

        if len(name_parts) == 2:
            # If query looks like "First Last", search for customers matching both parts
            results = Customers.objects.filter(
                Q(first_name__icontains=name_parts[0]) & Q(last_name__icontains=name_parts[1])
            )
        else:
            # Otherwise, search if the query matches first name, last name, or email
            results = Customers.objects.filter(
                Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(email__icontains=query)
            )

    # Pass the search query and results to the template for rendering
    context = {
        'query': query,
        'results': results,
    }
    return render(request, 'search_results.html', context)

